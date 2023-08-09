import tkinter as tk
import requests

# Create the main application window
root = tk.Tk()
root.title("Weather Forecast App")

# Configure background color
root.configure(bg="#3498db")

# Create and place UI elements with styles
label = tk.Label(root, text="Enter City:", font=("Helvetica", 16), bg="#3498db", fg="white")
label.pack(pady=10)

city_entry = tk.Entry(root, font=("Helvetica", 14))
city_entry.pack(padx=10, pady=5)

get_weather_button = tk.Button(root, text="Get Weather", font=("Helvetica", 14), bg="#2980b9", fg="white")
get_weather_button.pack(pady=10)

forecast_label = tk.Label(root, text="Weather Forecast:", font=("Helvetica", 16), bg="#3498db", fg="white")
forecast_label.pack(pady=10)

forecast_display = tk.Text(root, height=10, width=40, font=("Helvetica", 12))
forecast_display.pack(padx=10, pady=5)


# Function to fetch weather data from the API
def fetch_weather():
    api_key = "68085f669e10c3f6bd5d8bd1abecf89a"
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    weather_info = f"City: {data['name']}\n"
    weather_info += f"Temperature: {data['main']['temp']}°C\n"
    weather_info += f"Humidity: {data['main']['humidity']}%\n"
    weather_info += f"Conditions: {data['weather'][0]['description']}"

    forecast_display.delete(1.0, tk.END)  # Clear the display area
    forecast_display.insert(tk.END, weather_info)


# Connect the button to the fetch_weather function
get_weather_button.config(command=fetch_weather)

# Run the main loop
root.mainloop()
