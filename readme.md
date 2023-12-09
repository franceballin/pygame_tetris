# Проект по теме "PyGame" - "Tetris 2077"
## О проекте
**Tetris 2077** - это игра, созданная с помощью библиотеки *PyGame* на *Python*. Представляет собой стандартный тетрис в *киберпанк-стилистике*. Игрок погружается в *мир будущего*, где вместо обычных блоков используются элементы высокотехнологических объектов, символов киберпространства и геометрических фигур в стиле футуристических символов.
  
Геймплей сочетает в себе знакомую механику Тетриса с *эстетикой киберпанка*. Игрок управляет падающими блоками, поворачивая и располагая их так, чтобы создать заполненные горизонтальные линии и предотвратить достижение верха игрового поля. Визуальное оформление игры пропитано *яркими неоновыми цветами*, высокотехнологичными элементами и кибернетическими деталями, создавая *неповторимую атмосферу будущего*.

**Tetris 2077** предлагает игрокам уникальный опыт, сочетая в себе *ностальгию по классическому Тетрису* и *атмосферу киберпанка*, создавая захватывающее приключение в виртуальном мире будущего.
## Основная информация
При запуске приложения/кода игры, игрок встречает главное меню, где есть кнопки:
- "Начать игру", которая скрывает главное меню и открывает непосредственно тетрис
- "Настройки", где игрок может изменить скорость падения блоков, их внешний вид (и вид интерфейса в целом, вплоть до звукового сопровождения) и размер игрового поля.
- "Информация", где игрок может ознакомиться с идеей игры "Tetris 2077" и управлением.
- "Автор", где расположена информация об авторе проекта, и ссылка на GitHub.
- "Выход", с помощью которой игра закрывается.

Главное игровое поле состоит из множества клеток, где игрок управляет падающими фигурами, используя клавиши управления (WASD или стрелки). Фигуры, представленные в стиле высокотехнологичных объектов и символов киберпространства, падают сверху вниз, и игрок может вращать иили перемещать их влево/вправо для заполнения горизонтальных линий.

При заполнении целой горизонтальной линии, она исчезает, освобождая место для новых фигур и принося игроку очки. Игра продолжается до тех пор, пока фигуры не достигнут верхней части поля.

Код игры использует библиотеку Pygame для реализации графики, управления игровым процессом и взаймодействия с игроком. Вся логика игры, включая отслеживание очков, уровней сложности и геймплейные условия, реализована в соответствующих классах.
## Архитектура проекта
### Структура файлов и модулей:
- ```main.py``` - Главный файл, запускающий игру.
- ```game.py``` - Модуль, отвечающий за основной игровой процесс и его логику.
  - *Class Game*: Управление текущим игровым состоянием (начало, пауза, завершение), определение уровней, скорости падения блоков, подсчёт блоков и т.д.
- ```blocks.py``` - Модуль для определения различных блоков (фигур) и их характеристик.
  - *Class Block*: Описание свойств блоков (форма, цвет, движение).
- ```board.py``` - Модуль, отвечающий за отображение игрового поля.
  - *Class Board*: Управление графическим предоставлением игрового поля, отрисовка блоков и обработка коллизий.
- ```input_handler.py``` - Модуль для обработки пользовательского ввода.
  - *Class InputHandler*: Обработка действий игрока (управление блоками, пауза, завершение игры).
- ```settings.py``` - Файл с настройками игры (размер поля, цветовая палитра, скорость, звуковые эффекты и т.д.).
### Основные концепции и функции:
- **Инициализация игры**: Создание экземпляра игры и установка начальных параметров.
- **Цикл игры (Game Loop)**: Обновление экрана, обработка ввода игрока, обновление состояния игры и отображение изменений на экране.
- **Генерация блоков**: Создание и управление падающими блоками на основе определенных правил и случайной генерации.
- **Обработка коллизий**: Проверка столкновений блоков между собой и с границами поля.
- **Управление уровнями и скоростью**: Увеличение сложности и скорости игры с уровнем прохождения игроком определенного количества линий.
- **Система очков и рекордов**: Запись и отображение текущего счета игрока, а также сохранение лучших результатов.
### Организация кода:
- **Использование классов и объектно-ориентированного подхода**: Разделение функциональности на отдельные классы для лучшей организации кода и управления состояниями игры.
- **Модульность и чистота кода**: Разделение функций и методов по модулям для удобства чтения, тестирования и обслуживания кода.
- **Комментарии и документация**: Добавление пояснений и документации к основным функциям и классам для лучшего понимания кода другими разработчиками.

Такая архитектура позволяет легко масштабировать и поддерживать проект, а также обеспечит четкое разделение функциональности и легкость добавления новых элементов в игру.
