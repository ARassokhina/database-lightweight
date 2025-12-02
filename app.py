from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) # Разрешить CORS для фронтенда

# Настройка базы данных PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/database-light'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Определение модели данных для таблицы 'items'
class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.String(100), nullable=False)
    monthlyConsumption = db.Column(db.String(100), nullable=False)
    yearlyConsumption = db.Column(db.String(100), nullable=False)
    monthlyPrice = db.Column(db.String(100), nullable=False)
    yearlyPrice = db.Column(db.String(100), nullable=False)
    note = db.Column(db.String(255))

    def to_dict(self):
        return {
            'number': self.number,
            'name': self.name,
            'quantity': self.quantity,
            'monthlyConsumption': self.monthlyConsumption,
            'yearlyConsumption': self.yearlyConsumption,
            'monthlyPrice': self.monthlyPrice,
            'yearlyPrice': self.yearlyPrice,
            'note': self.note
        }

@app.route('/api/data', methods=['GET'])
def get_data():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])

if __name__ == '__main__':
    # Эта часть будет запускать приложение Flask, но создание БД и миграции будут выполнены отдельно
    app.run(debug=True, port=5000)

