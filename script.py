import matplotlib.pyplot as plt

# Здесь вы можете менять данные
data = {
    'ИЛЭ': 25,
    'СЭИ': 30,
    'ЭСЭ': 21,
    'ЛИИ': 22,
    'ЭИЭ': 18,
    'ЛСИ': 24,
    'СЛЭ': 17,
    'ИЭИ': 28,
    'СЭЭ': 15,
    'ИЛИ': 27,
    'ЛИЭ': 19,
    'ЭСИ': 21,
    'ЛСЭ': 17,
    'ЭИИ': 23,
    'ИЭЭ': 14,
    'СЛИ': 26
}

# Создание столбчатой диаграммы
types = list(data.keys())
counts = list(data.values())

plt.figure(figsize=(10, 6))
plt.bar(types, counts, color='skyblue')
plt.xlabel('Соционический Тип')
plt.ylabel('Количество людей')
plt.title('Статистика по типированиям по соционике сообщества My Typology')
plt.xticks(rotation=45)
plt.tight_layout()

# Сохранение диаграммы как изображения
image_path = 'sociotype_chart.png'
plt.savefig(image_path)
