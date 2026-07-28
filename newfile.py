import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

API_KEY = "6e180eada1859baad27e9e598ebdcf34"

class WeatherApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.city = TextInput(
            hint_text="Enter city name",
            multiline=False
        )

        btn = Button(text="Get Weather")
        btn.bind(on_press=self.get_weather)

        self.output = Label(text="Enter a city and press the button.")

        layout.add_widget(self.city)
        layout.add_widget(btn)
        layout.add_widget(self.output)

        return layout

    def get_weather(self, instance):
        city = self.city.text.strip()

        if not city:
            self.output.text = "Please enter a city name."
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        try:
            r = requests.get(url, timeout=10)
            data = r.json()

            if r.status_code == 200:
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                self.output.text = f"{city}\n🌡 {temp}°C\n☁ {desc}"
            else:
                self.output.text = "City not found."
        except Exception as e:
            self.output.text = str(e)

if __name__ == "__main__":
    WeatherApp().run()