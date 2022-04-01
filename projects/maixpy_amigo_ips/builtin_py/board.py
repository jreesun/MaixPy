try:
    import ujson as json
except ImportError:
    import json

config = json.loads("""
{
    "type": "amigo_ips",
    "lcd": {
        "height": 320,
        "width": 480,
        "invert": 1,
        "dir": 40,
        "lcd_type": 2,
        "touch": true,
        "font": [16, 24],
        "orientation": [1, 0]
    },
    "sensor":{
        "flipped": true,
        "lenses": false
    },
    "sdcard": {
        "sclk": 11,
        "mosi": 10,
        "miso": 6,
        "cs": 26
    },
    "board_info": {
        "BOOT_KEY": 16,
        "LED_R": 14,
        "LED_G": 15,
        "LED_B": 17,
        "LED_W": 32,
        "BACK": 31,
        "ENTER": 23,
        "NEXT": 20,
        "WIFI_TX": 6,
        "WIFI_RX": 7,
        "WIFI_EN": 8,
        "I2S0_MCLK": 13,
        "I2S0_SCLK": 21,
        "I2S0_WS": 18,
        "I2S0_IN_D0": 35,
        "I2S0_OUT_D2": 34,
        "I2C_SDA": 27,
        "I2C_SCL": 24,
        "SPI_SCLK": 11,
        "SPI_MOSI": 10,
        "SPI_MISO": 6,
        "SPI_CS": 12
    },
    "krux.pins": {
        "BUTTON_A": 16,
        "BUTTON_B": 20,
        "BUTTON_C": 23,
        "LED_W": 32
        "I2C_SDA": 27,
        "I2C_SCL": 24,
    }
}
""")
