import json
from decimal import Decimal #чтобы не было погрешностей от float
from sqlalchemy import(
    create_engine, #подключение к бд
    Column, #создание столбца таблицы
    Integer, #целое число
    String, #текст
    Numeric, #число с фикс точностью
    ForeignKey, #Создание внешнего ключа
    event#Обработка событий подключения к бд
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker #создание модели таблиц в виде питон классов, созд связи между моделями, созд инструмента для работы с бд

engine=create_engine("sqlite:///shop.db")

Base=declarative_base() #базовый класс

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True) #идентиф категории
    name = Column(String, unique=True, nullable=False) #название категории
    description= Column(String) # описание категорий
    
    products = relationship("Product", back_populates="category") #связь с товарами
    
class Product(Base):
    __tablename__= "products"
    
    id=Column(Integer, primary_key=True)
    name=Column(String, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    
    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False
    )
    
    category = relationship("Category", back_populates = "products") 
    
Base.metadata.create_all(engine)# создание таблицы

Session = sessionmaker(bind=engine) #создание сессии

with open("catalog.json", "r", encoding="utf-8") as file:
    data=json.load(file)
    
with Session.begin() as session:
    categories = {}
    
    for item in data:
        category_data = item["category"]
        category_name=category_data["name"]
        category_description=category_data["description"]
        
        if category_name not in categories:
            category = Category(
                name=category_name,
                description=category_description
            )
            
            session.add(category)
            
            categories[category_name]= category
        
        category=categories[category_name]
        
        product = Product(
            name=item["product_name"],
            price=Decimal(str(item["price"])),
            category=category
        )
        
        session.add(product)
        
print("gotovo")