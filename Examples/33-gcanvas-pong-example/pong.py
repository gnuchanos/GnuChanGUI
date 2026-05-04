"""
LGPL3+ — GCanvas sahne API + kutuphane ici tus (EnableSceneInput / InputBeginFrame / IsKeyDown).
Kontroller: W / S sol raket, Yukari / Asagi sag raket; canvas tiklayinca odak (tk, ayri bind gerekmez).
"""

import random

try:
    from GnuChanGUI import GnuChanGUI, GColors, Themecolors
except ImportError as e:
    raise ImportError("you need install GnuChanGUI") from e


class PongExample(GnuChanGUI):
    PADDLE_W = 14
    PADDLE_H = 80
    BALL_R = 9
    PADDLE_SPEED = 7
    BALL_SPEED = 6
    MARGIN = 16

    def __init__(
        self,
        Title="GCanvas Pong",
        Size=(780, 560),
        resizable=False,
        finalize=True,
        winPosX=1920 / 2,
        winPosY=1080 / 2,
    ):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)

        Themecolors().GnuChanOS
        self.C = GColors()

        self._inited = False
        self._cv = None

        self._arena_w = 700
        self._arena_h = 420
        self._left_y = 0.0
        self._right_y = 0.0
        self._ball_x = 0.0
        self._ball_y = 0.0
        self._ball_vx = float(self.BALL_SPEED)
        self._ball_vy = 3.0

        self._disp_ball = (0, 0)
        self._disp_left = (0, 0)
        self._disp_right = (0, 0)

        self.score_left = 0
        self.score_right = 0

        self.Layout = [
            [
                self.GText(
                    SetText="W / S = sol   |   Yukari / Asagi = sag   |   Canvas tikla (EnableSceneInput)",
                    SetValue="hint",
                    xStretch=True,
                    TFont="Sans, 11",
                )
            ],
            [
                self.GText(
                    SetText="0  -  0",
                    SetValue="score",
                    xStretch=True,
                    TPosition="center",
                    TFont="Sans, 22",
                )
            ],
            [
                self.GCanvas(
                    SetValue="game",
                    BColor="#0d1117",
                    Size=(88, 24),
                    xStretch=True,
                    yStretch=True,
                )
            ],
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout, Borderless=False, KeepOnTop=False)
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit, TimeOUT=12)

    def _pong_reset_ball(self, toward_right=None):
        self._ball_x = self._arena_w * 0.5
        self._ball_y = self._arena_h * 0.5
        if toward_right is True:
            self._ball_vx = float(self.BALL_SPEED)
        elif toward_right is False:
            self._ball_vx = -float(self.BALL_SPEED)
        else:
            self._ball_vx = float(self.BALL_SPEED) if random.random() > 0.5 else -float(self.BALL_SPEED)
        self._ball_vy = (random.random() * 2.0 - 1.0) * 4.0

    def _pong_init_scene(self, cv):
        w, h = cv.pixel_dimensions()
        if w < 120:
            w, h = self._arena_w, self._arena_h
        self._arena_w, self._arena_h = w, h

        self._left_y = (h - self.PADDLE_H) * 0.5
        self._right_y = self._left_y
        self._pong_reset_ball()

        lx = self.MARGIN
        rx = w - self.MARGIN - self.PADDLE_W

        cv.ClearScene2D()
        with cv.BeginScene2D():
            # tk 'width' anahtari eski GCanvas.DrawRectangle(width, height) ile cakisir; kalinlik icin outline yeter
            cv.DrawRectangle("bg", 0, 0, w, h, fill="#0d1117", outline="#30363d")
            cv.DrawLine("net", w // 2, 4, w // 2, h - 4, fill="#30363d", dash=(6, 6), width=2)
            cv.DrawRectangle(
                "paddle_L",
                lx,
                self._left_y,
                self.PADDLE_W,
                self.PADDLE_H,
                fill=self.C.blue6,
                outline="#58a6ff",
            )
            cv.DrawRectangle(
                "paddle_R",
                rx,
                self._right_y,
                self.PADDLE_W,
                self.PADDLE_H,
                fill=self.C.red4,
                outline="#ff7b72",
            )
            cv.DrawCircle(
                "ball",
                self._ball_x,
                self._ball_y,
                self.BALL_R,
                fill="#f0883e",
                outline="#ffa657",
                width=2,
            )

        self._disp_ball = (int(self._ball_x), int(self._ball_y))
        self._disp_left = (lx, int(self._left_y))
        self._disp_right = (rx, int(self._right_y))

        cv.EnableSceneInput(grab_focus=True, click_to_focus=True)

    def _paddle_rect(self, side):
        w = self._arena_w
        h = self._arena_h
        if side == "L":
            x = float(self.MARGIN)
            y = self._left_y
        else:
            x = float(w - self.MARGIN - self.PADDLE_W)
            y = self._right_y
        return x, y, float(self.PADDLE_W), float(self.PADDLE_H)

    def _ball_vs_paddle(self, px, py, pw, ph):
        bx, by, br = self._ball_x, self._ball_y, float(self.BALL_R)
        nearest_x = max(px, min(bx, px + pw))
        nearest_y = max(py, min(by, py + ph))
        dx = bx - nearest_x
        dy = by - nearest_y
        return (dx * dx + dy * dy) <= br * br

    def _pong_tick(self, cv):
        cv.InputBeginFrame()
        w, h = self._arena_w, self._arena_h
        pw, ph = float(self.PADDLE_W), float(self.PADDLE_H)

        if cv.IsKeyDown("w"):
            self._left_y -= self.PADDLE_SPEED
        if cv.IsKeyDown("s"):
            self._left_y += self.PADDLE_SPEED
        if cv.IsKeyDown("Up"):
            self._right_y -= self.PADDLE_SPEED
        if cv.IsKeyDown("Down"):
            self._right_y += self.PADDLE_SPEED

        self._left_y = max(4.0, min(self._left_y, h - ph - 4.0))
        self._right_y = max(4.0, min(self._right_y, h - ph - 4.0))

        self._ball_x += self._ball_vx
        self._ball_y += self._ball_vy

        br = float(self.BALL_R)
        if self._ball_y - br <= 2:
            self._ball_y = br + 2
            self._ball_vy = abs(self._ball_vy)
        elif self._ball_y + br >= h - 2:
            self._ball_y = h - br - 2
            self._ball_vy = -abs(self._ball_vy)

        lx, ly, lpw, lph = self._paddle_rect("L")
        rx, ry, rpw, rph = self._paddle_rect("R")

        if self._ball_vx < 0 and self._ball_vs_paddle(lx, ly, lpw, lph):
            self._ball_x = lx + lpw + br + 1.0
            self._ball_vx = abs(self._ball_vx)
            self._ball_vy += (self._ball_y - (ly + lph * 0.5)) * 0.08
        elif self._ball_vx > 0 and self._ball_vs_paddle(rx, ry, rpw, rph):
            self._ball_x = rx - br - 1.0
            self._ball_vx = -abs(self._ball_vx)
            self._ball_vy += (self._ball_y - (ry + rph * 0.5)) * 0.08

        self._ball_vy = max(-12.0, min(12.0, self._ball_vy))
        self._ball_vx = max(-14.0, min(14.0, self._ball_vx))

        if self._ball_x + br < 0:
            self.score_right += 1
            self._pong_reset_ball(toward_right=False)
        elif self._ball_x - br > w:
            self.score_left += 1
            self._pong_reset_ball(toward_right=True)

        nbx, nby = int(self._ball_x), int(self._ball_y)
        nlx, nly = int(lx), int(self._left_y)
        nrx, nry = int(rx), int(self._right_y)

        cv.MoveSceneObject("ball", nbx - self._disp_ball[0], nby - self._disp_ball[1])
        cv.MoveSceneObject("paddle_L", nlx - self._disp_left[0], nly - self._disp_left[1])
        cv.MoveSceneObject("paddle_R", nrx - self._disp_right[0], nry - self._disp_right[1])

        self._disp_ball = (nbx, nby)
        self._disp_left = (nlx, nly)
        self._disp_right = (nrx, nry)

        self.GetWindow["score"].update(f"{self.score_left}  -  {self.score_right}")

    def Update(self):
        if not self._inited:
            self._cv = self.GetWindow["game"]
            self._pong_init_scene(self._cv)
            self._inited = True
        else:
            self._pong_tick(self._cv)

    def BeforeExit(self):
        print("Pong kapandi.")


if __name__ == "__main__":
    PongExample()
