# GnuChanGUI

<p>lgpl3+ 4.61.0.206 Unreleased version</p>
<p>fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
this is lgpl3+ and this is hobby project not for money and i don't wanto bs license window to see</p>

i hope this become better one day

---

## kurulum

```
first install
pip install git+https://github.com/gnuchanos/gnuchangui

second install
1: download project .zip
2: extrack zip
3: cd gnuchangui
4: pip install .

# simple virtual environment
python -m venv .gcVENV
source .gcVENV/bin/activate
pip install .
```

---

## basit ornek

```python
from GnuChanGUI import GnuChanGUI

class DefaultExample(GnuChanGUI):
    def __init__(self):
        super().__init__(Title="Defaul Title", Size=(600, 300))

        self.Layout = [
            [self.GText(SetText="text", TPosition='c', xStretch=True, yStretch=True, SetValue="text")],
            [self.GButton(Text="button", SetValue="click")],
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(Update=self.Update)

    def Update(self):
        if "click" == self.GetEvent:
            self.GetWindow["text"].update("button pressed")

gc = DefaultExample()
```

---

## event sistemi

```
gc.GetEvent   = her sey event, button click, keyboard, input, multiline
gc.GetValues  = deger doner
gc.GetWindow[].update() = window icindeki her seyi gunceller
```

### keyboard
```python
# yeni keyboard event
self.d == self.CurrentKey  # tus basili tutma

# windows veya mac kullaniyorsaniz eski sistemi kullanin
# sorry but i don't like windows or mac this is only for gnu/linux
from GnuChanGUI import GKeyboard as GK

if self.GetEvent == GK().w:
    print("old keyboard event")

# yeni sistemde CurrentKey kullanilir
self.num2 == self.CurrentKey
```

### update widget
```python
if "Button" == gc.GetEvent:
    gc.GetWindow["Button"].update(gc.GetValues["ButtonNameChanger"])

# renk degistirme
GetWindow["button"].update(button_color = ("#9d4edd","#5a189a"))

# text degistirme
GetWindow["button"].update(GetWindow["text"].get())
```

---

## widget listesi

| Widget | ne ise yarar |
|--------|-------------|
| GText | yazi, `SetText` ile icerik |
| GButton | tus, `Text` ile yazi |
| GInput | tek satir input, `InText` ile varsayilan |
| GMultiline | cok satir input/output |
| GListBox | liste, `list` ile elemanlar |
| GTable | tablo, `TableLists` ile satirlar |
| GCheackBox | isaret kutusu, `CText` ile yazi, `GCheckBox` da ayni |
| GRadio | secenek, `groupID` ile grup |
| GSelection | acilir menu, `ListValues` ile liste |
| GIncreaseSelection | spin, `StartValue` ile baslangic |
| GSlider | slider, `SDirection` ile yon (h/v) |
| GProgressBar | progress bar, `PDirection` ile yon |
| GImage | resim, `filename` ile dosya |
| GImageGif | animasyonlu gif, `update_animation()` ile oynat |
| GGraph | vektor cizim, `draw_line`, `draw_circle` vb |
| GOutput | print ciktisini widget'a yonlendirir |
| GCanvas | 2D oyun/sahne, `BeginScene2D` ile cizim |
| GPanel | yeniden boyutlandirilabilir panel |
| GFrame | cerceveli container |
| GColumn | dikey container |
| GTabGroup / GTab | sekme arayuzu |
| GTitleBar | ozel baslik cubugu |
| GMenu | standart menu |
| GMenuForTheme | renklendirilebilir menu |

---

## GCanvas 2D API

```python
cv = self.GetWindow["canvas"]
with cv.BeginScene2D():
    cv.DrawRectangle("oyuncu", 0, 0, 40, 40, fill="teal")
    cv.DrawCircle("top", 100, 80, 12, fill="orange")
    cv.DrawText("skor: 0", 10, 10, fill="white")
    cv.DrawLine("cizgi", 0, 0, 200, 150, fill="red", width=2)
```

- `LoadSceneBatch([...])` ile toplu sahne yukleme
- `PickSceneObject(x, y)` ile tiklama
- `SelectSceneObject(name)` ile secim
- `MoveSceneObject(name, dx, dy)` ile hareket
- `EnableSceneInput()` ile klavye girdisi

---

## temalar

```python
from GnuChanGUI import Themecolors, GColors, GnuChanOSColor

# built-in temalar
Themecolors().GnuChanOS    # mor tema (default)
Themecolors().Black        # siyah tema
Themecolors().Blue         # mavi tema
Themecolors().Red          # kirmizi tema
Themecolors().Green        # yesil tema
```

### renk paleti
```python
c = GColors()           # tum renkler (8 cesit kirmizi, yesil, mavi, sari, turuncu, pembe, mor, turkuaz, gri)
c_os = GnuChanOSColor() # gnuchanos marka renkleri
```

### ozel tema
```python
Themecolors().GnuChanOS(
    themeName="MyTheme",
    text="#ffffff",
    background="#1a1a2e",
    input="#16213e",
    text_input="#ffffff",
    scroll="#a7a7a7",
    button=("#ffffff", "#383838"),
    progress=("#ffffff", "#383838"),
    border=0, slider_depth=0, progress_depth=0
)
```

---

## klavye tuslari

```python
# harfler
self.A, self.B, ..., self.Z

# sayilar
self.ZERO, self.ONE, ..., self.NINE

# fonksiyon tuslari
self.F1, self.F2, ..., self.F12

# yon tuslari
self.LEFT, self.RIGHT, self.UP, self.DOWN

# navigasyon
self.ENTER, self.ESCAPE, self.SPACE, self.TAB
self.BACKSPACE, self.DELETE, self.INSERT
self.HOME, self.END, self.PAGE_UP, self.PAGE_DOWN

# modifier
self.CONTROL, self.SHIFT, self.ALT, self.META

# kombinasyon
self.CTRL_A, self.CTRL_C, self.CTRL_V, self.CTRL_X
self.CTRL_Z, self.CTRL_S, self.CTRL_O
self.CTRL_SHIFT_S, self.CTRL_ALT_DELETE
```

---

## pencere ozellikleri

```python
# her zaman ustte / saydam
self.WindowONTOP(transparancy=0.85)
self.StillONTOP_UnderUpdate()

# her zaman altta / saydam
self.WindowONBOTTOM(transparancy=0.85)
self.StillONBOTTOM_UnderUpdate()

# cercevesiz pencere
self.GWindow(SetMainWindowLayout_List=layout, Borderless=True)

# pencere hazir mi kontrol
self.IsWindowReady()
```

---

## ornekler

Finish Examples

| Example | Finish? |
|---------|---------|
| Simple Timer | Fimish |
| Simple Calculator | Fimish |
| Simple Text Editor | Fimish |
| Simple Program Runner Like Rofi | Fimish |
| Simple Video and Music Download from Youtube | Fimish |
| Simple Video to Sound convert | Fimish |
| Simple Music Player | Fimish |
| Simple Wine Manager | not Fimish??? |
| Simple Game (1 level demo) | Fimish (but have keyboard delay :@) |

Tutorials var `Examples/Tutorials/` klasorunde.

---

## onemli notlar

- bu kutuphane **gnu/linux** icin. windows veya mac kullaniyorsan eski keyboard modulunu kullan (`GKeyboard_Winows`)
- PySimpleGUI uzerine kurulu (tkinter port)
- python ogrenirken yapilmis bir hobi projesi, beginner seviyesi
- lisans **LGPL-3.0+**

---

## baglantilar

- github: https://github.com/gnuchanos/GnuChanGUI
- author: @archkubi
