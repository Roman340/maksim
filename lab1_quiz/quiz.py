import json, os, datetime 
 
QUESTIONS = [ 
    {"q": "Какая команда запускает контейнер?", 
     "options": ["docker run", "docker go", "docker exec -d"], "answer": 0}, 
    {"q": "Что хранит реестр образов (Docker Hub)?", 
     "options": ["Логи контейнеров", "Образы", "Пароли пользователей"], "answer": 1}, 
    {"q": "Что произойдёт с файлами контейнера после его удаления (без тома)?", 
     "options": ["Сохранятся навсегда", "Исчезнут вместе с контейнером", 
                 "Перенесутся в новый контейнер"], "answer": 1}, 
    {"q": "Какой флаг пробрасывает порт на хост?", 
     "options": ["-p", "-v", "-e"], "answer": 0}, 
    {"q": "Что такое том (volume)?", 
     "options": ["Единица измерения памяти", 
                 "Папка хоста, подключённая внутрь контейнера", 
                 "Специальный вид образа"], "answer": 1}, 
] 
 
def main(): 
    name = input("Ваше имя: ").strip() or "anonymous" 
    score = 0 
    for i, item in enumerate(QUESTIONS, 1): 
        print(f"\nВопрос {i}: {item['q']}") 
        for n, opt in enumerate(item["options"], 1): 
            print(f"  {n}) {opt}") 
        while True: 
            try: 
                ans = int(input("Ваш ответ (номер): ")) 
                if 1 <= ans <= len(item["options"]): 
                    break 
            except ValueError: 
                pass 
            print("Введите номер варианта!") 
        if ans - 1 == item["answer"]: 
            score += 1 
            print("Верно!") 
        else: 
            print(f"Неверно. Правильный ответ: {item['options'][item['answer']]}") 
    print(f"\n{name}, ваш результат: {score} из {len(QUESTIONS)}") 
    results = [] 
    if os.path.exists("results.json"): 
        with open("results.json", "r", encoding="utf-8") as f: 
            results = json.load(f) 
    results.append({"name": name, "score": score, "total": len(QUESTIONS), 
                    "date": datetime.datetime.now().isoformat(timespec="seconds")}) 
    with open("results.json", "w", encoding="utf-8") as f: 
        json.dump(results, f, ensure_ascii=False, indent=2) 
    print("Результат сохранён в results.json") 
 
if __name__ == "__main__": 
    main() 