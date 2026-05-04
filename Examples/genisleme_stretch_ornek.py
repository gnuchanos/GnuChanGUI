"""Genisleme (stretch) — yatay: xStretch / xStretch_weight; dikey: yStretch + yStretch_row_weight.

Yatay: ayni satirda xStretch_weight ile oran.
Dikey: farkli LAYOUT satirlarinda yStretch_row_weight (gcLibrary: expand_weight_row) ile
ekstra yukseklik orani — en az bir satirda bu parametre verilirse tum form satirlari
grid ile istiflenir; verilmeyen genisleyen satirlar agirlik 1 alir.

Calistirma (repo kokunden):
  python Examples/genisleme_stretch_ornek.py
"""
try:
    from GnuChanGUI import GnuChanGUI, GColors, Themecolors
except ImportError as e:
    raise ImportError("GnuChanGUI yuklu degil.") from e


class GenislemeStretchOrnek(GnuChanGUI):
    def __init__(self, Title="Genisleme — yatay + dikey agirlik", Size=(880, 560), resizable=True, finalize=True, winPosX=880, winPosY=420):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)
        Themecolors().GnuChanOS
        c = GColors()

        aciklama = [
            self.GText(
                SetText=(
                    ">>> YATAY: pencereyi genisletin. DIKEY: yuksekligi degistirin. "
                    "Asagida iki blok var: ust yStretch_row_weight=1, alt =3 (fazla yuksekligin ~3/4'u altta)."
                ),
                TFont="Sans, 12",
                xStretch=True,
                TPosition="c",
                BColor=c.yellow7,
                EmptySpace=(8, 10),
            )
        ]

        # Yatay: 1 : 2 : 1 — yStretch kapali ki dikey agirlik sadece asagidaki iki satira kalsin
        sira_agirlikli = [
            self.GText(
                SetText="1 pay\n(xStretch_weight=1)",
                TFont="Sans, 16",
                TPosition="c",
                xStretch=True,
                xStretch_weight=1,
                BColor=c.blue5,
                EmptySpace=(6, 16),
            ),
            self.GText(
                SetText="2 pay\n(ORTA)",
                TFont="Sans, 16",
                TPosition="c",
                xStretch=True,
                xStretch_weight=2,
                BColor=c.orange4,
                EmptySpace=(6, 16),
            ),
            self.GText(
                SetText="1 pay\n(xStretch_weight=1)",
                TFont="Sans, 16",
                TPosition="c",
                xStretch=True,
                xStretch_weight=1,
                BColor=c.blue5,
                EmptySpace=(6, 16),
            ),
        ]

        sira_esit = [
            self.GText(
                SetText="Esit A",
                TFont="Sans, 14",
                TPosition="c",
                xStretch=True,
                BColor=c.pink2,
                EmptySpace=(6, 12),
            ),
            self.GText(
                SetText="Esit B",
                TFont="Sans, 14",
                TPosition="c",
                xStretch=True,
                BColor=c.pink4,
                EmptySpace=(6, 12),
            ),
            self.GText(
                SetText="Esit C",
                TFont="Sans, 14",
                TPosition="c",
                xStretch=True,
                BColor=c.pink6,
                EmptySpace=(6, 12),
            ),
        ]

        sira_1_3 = [
            self.GText(
                SetText="Dar (w=1)",
                TFont="Sans, 14",
                TPosition="c",
                xStretch=True,
                xStretch_weight=1,
                BColor=c.navy3,
                TColor=c.yellow7,
                EmptySpace=(6, 10),
            ),
            self.GText(
                SetText="Genis (w=3)",
                TFont="Sans, 14",
                TPosition="c",
                xStretch=True,
                xStretch_weight=3,
                BColor=c.green4,
                EmptySpace=(6, 10),
            ),
        ]

        # Dikey agirlik: bu satirda herhangi bir ogeye yStretch_row_weight vermek yeterli (tum form satirlari grid'e gecer)
        dikey_baslik = [
            self.GText(
                SetText="--- Dikey pay (yStretch + yStretch_row_weight) ---",
                TFont="Sans, 11",
                xStretch=True,
                BColor=c.navy6,
                TColor=c.yellow7,
            )
        ]
        satir_ince = [
            self.GText(
                SetText="Ust blok (yStretch_row_weight=1)\nyStretch=True",
                TFont="Sans, 13",
                TPosition="c",
                xStretch=True,
                yStretch=True,
                yStretch_row_weight=1,
                BColor=c.blue3,
                EmptySpace=(8, 8),
            )
        ]
        satir_genis = [
            self.GMultiline(
                InText="Alt blok (yStretch_row_weight=3).\nPencereyi dikey buyutun; bu alan usttekinden cok daha fazla yukseklik alir (oran 1:3).",
                SetValue="ml_dikey",
                Size=(40, 4),
                TFont="Sans, 12",
                xStretch=True,
                yStretch=True,
                yStretch_row_weight=3,
                BColor=c.green6,
                TColor=c.black,
                NoScroolBar=True,
            )
        ]

        self.Layout = [
            aciklama,
            [self.GHSep()],
            [
                self.GText(
                    SetText="1 : 2 : 1 (xStretch_weight)",
                    TFont="Sans, 11",
                    xStretch=True,
                    BColor=c.navy6,
                    TColor=c.yellow7,
                )
            ],
            sira_agirlikli,
            [self.GHSep()],
            [
                self.GText(
                    SetText="Esit xStretch (agirlik yok)",
                    TFont="Sans, 11",
                    xStretch=True,
                )
            ],
            sira_esit,
            [self.GHSep()],
            [
                self.GText(
                    SetText="1 : 3 (xStretch_weight)",
                    TFont="Sans, 11",
                    xStretch=True,
                )
            ],
            sira_1_3,
            [self.GHSep()],
            dikey_baslik,
            satir_ince,
            satir_genis,
            [
                self.GButton(Text="Kapat", SetValue="kapat"),
            ],
        ]
        self.GWindow(SetMainWindowLayout_List=self.Layout, KeepOnTop=False)
        self.SetUpdate(Update=self._update, exitBEFORE=self._exit)

    def _update(self):
        if self.GetEvent == "kapat":
            self.closeWindow = True

    def _exit(self):
        print("Genisleme ornek cikis")


if __name__ == "__main__":
    GenislemeStretchOrnek()
