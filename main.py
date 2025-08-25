from kivy.app import App
from kivy.uix.button import Button
from plyer import fingerprint

class FingerApp(App):
    def build(self):
        btn = Button(text="Scanner empreinte")
        btn.bind(on_release=self.scan)
        return btn

    def scan(self, instance):
        try:
            if fingerprint.authenticate():
                instance.text = "Empreinte OK ✅"
            else:
                instance.text = "Échec ❌"
        except NotImplementedError:
            instance.text = "Fingerprint non disponible"

if __name__ == "__main__":
    FingerApp().run()
