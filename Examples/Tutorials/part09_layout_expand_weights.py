"""Part 09 — xStretch_weight / yStretch_weight (satir icinde orantili genislik).

Genisleme ornegi (yatay + dikey agirlik): python Examples/genisleme_stretch_ornek.py

Bu dosya daha cok eleman turu (GColumn, GFrame, GTabGroup, Multiline) icerir.
Dikey satir agirligi: yStretch_row_weight (gcLibrary expand_weight_row).
Ayni satirda birden fazla oge xStretch=True iken agirlik yoksa fazla alan
genelde esit paylasilir; xStretch_weight verilince oranlidir.

Pencereyi yatay buyutup kucultun: ozellikle 1:3:1 ve 1:4:1 satirlarini karsilastirin.

Calistirma (repo kokunden):
  python Examples/Tutorials/part09_layout_expand_weights.py
"""
try:
    from GnuChanGUI import GnuChanGUI, GColors, Themecolors
except ImportError as e:
    raise ImportError("GnuChanGUI yuklu degil; pip install veya PYTHONPATH ile ekleyin.") from e


class Part09(GnuChanGUI):
    def __init__(self, Title="Part 09 — xStretch_weight / yStretch_weight", Size=(720, 520), resizable=True, finalize=True, winPosX=900, winPosY=480):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)
        Themecolors().GnuChanOS
        self.C = GColors()

        # --- 1:3:1 metin panelleri (agirlikli) ---
        row_weighted_text = [
            self.GText(
                SetText="w=1",
                TPosition="c",
                xStretch=True,
                xStretch_weight=1,
                BColor=self.C.blue5,
                EmptySpace=(4, 4),
            ),
            self.GText(
                SetText="w=3 (orta genisler)",
                TPosition="c",
                xStretch=True,
                xStretch_weight=3,
                BColor=self.C.yellow3,
                EmptySpace=(4, 4),
            ),
            self.GText(
                SetText="w=1",
                TPosition="c",
                xStretch=True,
                xStretch_weight=1,
                BColor=self.C.green5,
                EmptySpace=(4, 4),
            ),
        ]

        # --- Esit pay (agirlik yok; klasik pack davranisi) ---
        row_equal_no_weights = [
            self.GText(SetText="esit A", TPosition="c", xStretch=True, BColor=self.C.pink1, EmptySpace=(4, 4)),
            self.GText(SetText="esit B", TPosition="c", xStretch=True, BColor=self.C.pink3, EmptySpace=(4, 4)),
            self.GText(SetText="esit C", TPosition="c", xStretch=True, BColor=self.C.pink5, EmptySpace=(4, 4)),
        ]

        # --- GColumn ile 1 : 4 : 1 ---
        col_narrow_l = self.GColumn(
            winColumnLayout_List=[[self.GText(SetText="Kolon L", xStretch=True, TPosition="c")], [self.GButton(Text="L", SetValue="l")]],
            xStretch=True,
            xStretch_weight=1,
            yStretch=True,
            BColor=self.C.blue8,
        )
        col_wide = self.GColumn(
            winColumnLayout_List=[
                [self.GText(SetText="Orta kolon (w=4)", xStretch=True, TPosition="c")],
                [self.GButton(Text="Orta", SetValue="mid")],
            ],
            xStretch=True,
            xStretch_weight=4,
            yStretch=True,
            BColor=self.C.purple3,
        )
        col_narrow_r = self.GColumn(
            winColumnLayout_List=[[self.GText(SetText="Kolon R", xStretch=True, TPosition="c")], [self.GButton(Text="R", SetValue="r")]],
            xStretch=True,
            xStretch_weight=1,
            yStretch=True,
            BColor=self.C.blue8,
        )
        row_columns_weighted = [col_narrow_l, col_wide, col_narrow_r]

        # --- GFrame agirlik: sol ince cerceve, sag daha genis ---
        frame_small = self.GFrame(
            GFText="F w=1",
            InsideWindowLayout=[[self.GText(SetText="icerik", xStretch=True)]],
            xStretch=True,
            xStretch_weight=1,
            yStretch=True,
            BColor=self.C.green8,
            Border=1,
            SetValue="frS",
        )
        frame_large = self.GFrame(
            GFText="F w=2",
            InsideWindowLayout=[[self.GText(SetText="daha genis cerceve alani", xStretch=True)]],
            xStretch=True,
            xStretch_weight=2,
            yStretch=True,
            BColor=self.C.green4,
            Border=1,
            SetValue="frL",
        )
        row_frames = [frame_small, frame_large]

        # --- Etiket (w=1) + Multiline (w=3) ---
        row_label_ml = [
            self.GText(
                SetText="Not:",
                TPosition="n",
                xStretch=True,
                xStretch_weight=1,
                BColor=self.C.navy2,
                EmptySpace=(4, 4),
            ),
            self.GMultiline(
                InText="Multiline w=3.\nPencereyi genisletin; bu kutu metin satirina gore sol etiketten daha fazla yer kaplar.",
                SetValue="ml",
                Size=(24, 5),
                xStretch=True,
                xStretch_weight=3,
                yStretch=True,
                BColor=self.C.yellow7,
                TColor=self.C.black,
            ),
        ]

        tab_a = [[self.GText(SetText="Sekme A", xStretch=True, TPosition="c", BColor=self.C.yellow5)]]
        tab_b = [[self.GText(SetText="Sekme B", xStretch=True, TPosition="c", BColor=self.C.orange3)]]
        tabs = self.GTabGroup(
            TabGroupLayout=[
                [self.GTab(Text="A", TabLayout=tab_a, SetValue="tA")],
                [self.GTab(Text="B", TabLayout=tab_b, SetValue="tB")],
            ],
            SetValue="tabsW",
            Size=(None, 140),
            xStretch_weight=2,
        )
        row_tab_weighted = [
            self.GText(
                SetText="Sekme grubu\n(w=2)",
                TPosition="c",
                xStretch=True,
                xStretch_weight=1,
                BColor=self.C.navy5,
            ),
            tabs,
        ]

        self.Layout = [
            [
                self.GText(
                    SetText="Part 09: Agirlikli genislik — pencereyi YATAY yeniden boyutlandirin.",
                    xStretch=True,
                    TPosition="c",
                    SetValue="hdr",
                )
            ],
            [self.GHSep()],
            [self.GText(SetText="Ust satir: GText 1 : 3 : 1 (xStretch_weight)", xStretch=True)],
            row_weighted_text,
            [self.GHSep()],
            [self.GText(SetText="Karsilastirma: uc GText, hepsi xStretch, agirlik YOK (esit)", xStretch=True)],
            row_equal_no_weights,
            [self.GHSep()],
            [self.GText(SetText="GColumn 1 : 4 : 1", xStretch=True)],
            row_columns_weighted,
            [self.GHSep()],
            [self.GText(SetText="GFrame 1 : 2", xStretch=True)],
            row_frames,
            [self.GHSep()],
            [self.GText(SetText="GText + GMultiline (1:3)", xStretch=True)],
            row_label_ml,
            [self.GHSep()],
            [self.GText(SetText="GText + GTabGroup (1:2) — sekme alani daha genis pay alir", xStretch=True)],
            row_tab_weighted,
            [self.GText(SetText="Durum", SetValue="status", xStretch=True)],
        ]
        self.GWindow(SetMainWindowLayout_List=self.Layout, KeepOnTop=False)
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        ev = self.GetEvent
        if ev in ("l", "mid", "r", "tA", "tB"):
            self.GetWindow["status"].update("Olay: {}".format(ev))

    def BeforeExit(self):
        print("Part 09 cikis")


if __name__ == "__main__":
    Part09()
