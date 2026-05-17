"""ALL_IN_ONE.py — Tüm GnuChanGUI widget örneklerini tek pencerede gösterir."""

try:
    from GnuChanGUI import GnuChanGUI, GnuChanOSColor, GColors, Themecolors
except ImportError as e:
    raise ImportError("GnuChanGUI yüklü değil.") from e


class AllInOne(GnuChanGUI):
    def __init__(self, Title="ALL IN ONE - Widget Demo", Size=(980, 720), resizable=True, finalize=True):
        super().__init__(Title, Size, resizable, finalize)
        Themecolors().GnuChanOS

        self.CGC = GnuChanOSColor()
        self.C   = GColors()

        tab1 = [
            [self.GText(SetText="Tab 1: Giriş ve Butonlar", TFont="Sans, 16", TPosition="center", xStretch=True)],
            [self.GInput(InText="Tab 1 girişi", SetValue="tab_input", xStretch=True)],
            [self.GButton(Text="Tab 1 Kaydet", SetValue="tab1_save", xStretch=True)]
        ]

        tab2 = [
            [self.GText(SetText="Tab 2: Liste ve Seçim", TFont="Sans, 16", TPosition="center", xStretch=True)],
            [self.GListBox(list=["Secenek 1", "Secenek 2", "Secenek 3"], SetValue="tab_list", Size=(20, 6), xStretch=True, yStretch=True)],
            [self.GSelection(ListValues=["A", "B", "C"], DefaultValue="B", SetValue="tab_combo", xStretch=True)]
        ]

        tab3 = [
            [self.GText(SetText="Tab 3: Kontroller", TFont="Sans, 16", TPosition="center", xStretch=True)],
            [
                self.GCheackBox(CText="Seçenek X", SetValue="tab_chk_x"),
                self.GCheackBox(CText="Seçenek Y", SetValue="tab_chk_y"),
                self.GCheackBox(CText="Seçenek Z", SetValue="tab_chk_z"),
            ],
            [
                self.GRadio(RText="Radyo A", groupID="TAB_RAD", SetValue="tab_rad_a"),
                self.GRadio(RText="Radyo B", groupID="TAB_RAD", SetValue="tab_rad_b"),
            ]
        ]

        tab1 = [
            [self.GText(SetText="Giriş ve Metin", TFont="Sans, 16", TPosition="center", xStretch=True)],
            [self.GText(SetText="Tek Satır Giriş", SetValue="lbl_input")],
            [self.GInput(InText="Buraya yazın...", SetValue="input", xStretch=True, Size=(None, 30))],
            [self.GText(SetText="Çok Satırlı Metin", SetValue="lbl_multi")],
            [self.GMultiline(InText="Merhaba!\nBu bir GMultiline örneğidir.", SetValue="multi", xStretch=True, yStretch=True, Size=(None, 8), TFont="Sans, 12")],
            [self.GButton(Text="Temizle", SetValue="clear", xStretch=True)],
        ]

        tab2 = [
            [self.GText(SetText="Seçimler ve Kontroller", TFont="Sans, 16", TPosition="center", xStretch=True)],
            [self.GText(SetText="Checkboxler", SetValue="lbl_checkbox")],
            [
                self.GCheackBox(CText="Seçenek A", SetValue="chkA", EmptySpace=(5, 5)),
                self.GCheackBox(CText="Seçenek B", SetValue="chkB", EmptySpace=(5, 5)),
                self.GCheackBox(CText="Seçenek C", SetValue="chkC", EmptySpace=(5, 5)),
            ],
            [self.GText(SetText="Radyo Seçimleri", SetValue="lbl_radio")],
            [
                self.GRadio(RText="Radio 1", groupID="RAD", SetValue="rad1"),
                self.GRadio(RText="Radio 2", groupID="RAD", SetValue="rad2"),
                self.GRadio(RText="Radio 3", groupID="RAD", SetValue="rad3"),
            ],
            [self.GText(SetText="Açılır Liste ve Spin", SetValue="lbl_select")],
            [self.GSelection(ListValues=["Kırmızı", "Yeşil", "Mavi"], DefaultValue="Yeşil", SetValue="combo", xStretch=True)],
            [self.GIncreaseSelection(ListValues=[1, 2, 3, 4, 5, 6], StartValue=1, SetValue="spin", Size=(80, None), xStretch=True)]
        ]

        tab3 = [
            [self.GText(SetText="Liste ve Tablo", TFont="Sans, 16", TPosition="center", xStretch=True)],
            [
                self.GListBox(list=["Elma", "Armut", "Üzüm", "Muz", "Kiraz"], SetValue="listbox", Size=(20, 6), xStretch=True, yStretch=True),
                self.GTable(TableLists=[
                    ["Ürün", "Adet", "Durum"],
                    ["Elma", "12", "Stok"],
                    ["Armut", "5", "Stok"],
                    ["Üzüm", "0", "Tükendi"],
                    ["Muz", "8", "Stok"],
                ], SetValue="table", VisibleRows=6),
            ],
            [self.GSlider(MaxRange=(0, 100), DefaultValue=30, SetValue="slider", xStretch=True)],
            [self.GProgressBar(MaxRange=100, SetValue="progress", PDirection="h", xStretch=True)],
            [self.GButton(Text="Durumu Güncelle", SetValue="update", xStretch=True)],
        ]

        self.Layout = [
            [self.GText(SetText="ALL IN ONE - Sekmeli Widget Demo", TFont="Sans, 22", TPosition="center", xStretch=True, BColor=self.CGC.FColors1)],
            [
                self.GTabGroup(
                    TabGroupLayout=[
                        [self.GTab(Text="Giriş", TabLayout=tab1, SetValue="tab1")],
                        [self.GTab(Text="Kontroller", TabLayout=tab2, SetValue="tab2")],
                        [self.GTab(Text="Liste/Tablo", TabLayout=tab3, SetValue="tab3")],
                    ],
                    SetValue="tabG",
                    Size=(None, 420),
                    xStretch_weight=True,
                    yStretch_weight=True,
                )
            ],
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout, KeepOnTop=False)
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        if self.GetEvent is None or not self.GetValues:
            return

        if self.GetEvent == "update":
            self.GetWindow["progress"].update(self.GetValues.get("slider", 0))
            self.GetWindow["status"].update(
                "Input: {}\nCombo: {}\nSpin: {}\nSlider: {}\nCheckboxler: {}, {}, {}\nRadio: {}\nListbox: {}\nTablo seçimi: {}".format(
                    self.GetValues.get("input", ""),
                    self.GetValues.get("combo", ""),
                    self.GetValues.get("spin", ""),
                    self.GetValues.get("slider", 0),
                    self.GetValues.get("chkA", False),
                    self.GetValues.get("chkB", False),
                    self.GetValues.get("chkC", False),
                    self.GetEvent if self.GetEvent in ("rad1", "rad2", "rad3") else self._current_radio(),
                    self.GetValues.get("listbox", []),
                    self.GetValues.get("table", []),
                )
            )

        if self.GetEvent == "clear":
            self.GetWindow["input"].update("")
            self.GetWindow["multi"].update("")
            self.GetWindow["chkA"].update(False)
            self.GetWindow["chkB"].update(False)
            self.GetWindow["chkC"].update(False)
            self.GetWindow["combo"].update("Kırmızı")
            self.GetWindow["spin"].update(1)
            self.GetWindow["slider"].update(0)
            self.GetWindow["progress"].update(0)
            self.GetWindow["status"].update("Tüm alanlar temizlendi.")

    def _current_radio(self):
        if self.GetValues.get("rad1"):
            return "Radio 1"
        if self.GetValues.get("rad2"):
            return "Radio 2"
        if self.GetValues.get("rad3"):
            return "Radio 3"
        return "(seçilmedi)"

    def BeforeExit(self):
        print("ALL IN ONE örneği kapatılıyor.")


if __name__ == "__main__":
    AllInOne()
