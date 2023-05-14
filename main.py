from flask import Flask, render_template

app = Flask(__name__)

car_data = {
    'Maruti': ['Swift', 'Wagon', '800', 'Zen', 'Ertiga', 'Alto', 'SX4', 'Baleno', 'Omni', 'Vitara', 'Ciaz', 'Celerio', 'Eeco', 'Ritz', 'Ignis', 'A-Star', 'Estilo', 'S-Cross', 'Esteem', 'XL6', 'Dzire', 'Gypsy', 'S-Presso'],
    'Skoda': ['Rapid', 'Superb', 'Octavia', 'Yeti', 'Fabia', 'Laura', 'Kodiaq'],
    'Honda': ['City', 'WR-V', 'Amaze', 'Jazz', 'Brio', 'CR-V', 'Civic', 'BR-V', 'Accord', 'Mobilio', 'BRV'],
    'Hyundai': ['i20', 'Xcent', 'Verna', 'i10', 'Creta', 'Santro', 'Elantra', 'Grand', 'Getz', 'Elite', 'Accent', 'EON', 'Santa', 'Sonata', 'Tucson', 'Venue'],
    'Toyota': ['Etios', 'Fortuner', 'Innova', 'Corolla', 'Glanza', 'Camry', 'Yaris', 'Qualis', 'Premio', 'Platinum', 'Land'],
    'Ford': ['Figo', 'EcoSport', 'Freestyle', 'Fiesta', 'Classic', 'Ecosport', 'Endeavour', 'Fusion', 'Aspire', 'Ikon'],
    'Renault': ['Duster', 'KWID', 'Triber', 'Scala', 'Lodgy', 'Pulse', 'Fluence', 'Captur', 'Koleos'],
    'Mahindra': ['KUV', 'Verito', 'Scorpio', 'XUV500', 'Ssangyong', 'Quanto', 'Marazzo', 'Thar', 'Bolero', 'Willys', 'XUV300', 'TUV', 'Xylo', 'NuvoSport', 'Jeep', 'Supro', 'Ingenio', 'Renault', 'Logan', 'Marshal'],
    'Tata': ['Tigor', 'Safari', 'Manza', 'Indica', 'Indigo', 'Nexon', 'Zest', 'Hexa', 'Tiago', 'Sumo', 'New', 'Nano', 'Venture', 'Aria', 'Bolt', 'Xenon', 'Estate', 'Harrier', 'Winger', 'Spacio'],
    'Chevrolet': ['Enjoy', 'Beat', 'Captiva', 'Sail', 'Tavera', 'Aveo', 'Spark', 'Optra', 'Cruze', 'Trailblazer'],
    'Fiat': ['Palio', 'Grande', 'Linea', 'Punto', 'Avventura'],
    'Datsun': ['GO', 'RediGO'],
    'Jeep': ['Compass', 'Wrangler'],
    'Mercedes-Benz': ['B', 'New', 'S-Class', 'E-Class', 'CLA', 'GL-Class', 'GLA', 'M-Class', 'GLC'],
    'Mitsubishi': ['Pajero', 'Lancer'],
    'Audi': ['A6', 'Q5', 'Q7', 'A4', 'Q3', 'A3'],
    'Volkswagen': ['Ameo', 'Vento', 'Polo', 'Passat', 'GTI', 'Jetta', 'Multivan', 'CrossPolo'],
    'BMW': ['X1', '5', 'X4', '3', 'X6', '6', '7', 'X7', 'X3', 'X5'],
    'Nissan': ['Terrano', 'Sunny', 'Micra', 'Kicks', 'Teana'],
    'Lexus': ['ES'],
    'Jaguar': ['XF', 'XE'],
    'Land': ['Rover'],
    'MG': ['Hector'],
    'Volvo': ['XC40', 'XC90', 'V40', 'S60', 'XC60', 'S90'],
    'Daewoo': ['Matiz'],
    'Kia': ['Seltos'],
    'Force': ['Gurkha', 'One'],
    'Ambassador': ['CLASSIC', 'Classic', 'Grand'],
    'Ashok': ['Leyland'],
    'Isuzu': ['MUX', 'D-Max', 'MU'],
    'Opel': ['Astra'],
    'Peugeot': ['309']}

brands = list(car_data.keys())

@app.route("/")
def index():
    return render_template("index.html", car_data=car_data, brands = brands)


if __name__ == "__main__":
    app.run(debug=True)

