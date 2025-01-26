class Quiz:
    ''' Stores questions and answers '''
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer
    

quizzes = [
    {
        "question": "What is the name of the protagonist in *The Legend of Zelda* series?",
        "options": ["Zelda", "Link", "Ganon"],
        "answer": "Link"
    },
    {
        "question": "In *Super Mario Bros.*, what was Mario’s original profession?",
        "options": ["Plumber", "Chef", "Carpenter"],
        "answer": "Plumber"
    },
    {
        "question": "Which Pokémon game introduced the region of Galar?",
        "options": ["*Pokémon Sun & Moon*", "*Pokémon Sword & Shield*", "*Pokémon X & Y*"],
        "answer": "*Pokémon Sword & Shield*"
    },
    {
        "question": "What is the name of the first *Animal Crossing* game released outside Japan?",
        "options": ["*Animal Crossing: Wild World*", "*Animal Crossing: Population Growing!*", "*Animal Crossing: New Horizons*"],
        "answer": "*Animal Crossing: Population Growing!*"
    },
    {
        "question": "Which Nintendo character uses a parasol as a weapon in *Super Smash Bros.*?",
        "options": ["Peach", "Daisy", "Rosalina"],
        "answer": "Peach"
    },
    {
        "question": "In *God of War (2018)*, what mythological realm is Kratos’ wife from?",
        "options": ["Vanaheim", "Jötunheim", "Alfheim"],
        "answer": "Jötunheim"
    },
    {
        "question": "Which PlayStation-exclusive game features a protagonist named Jin Sakai?",
        "options": ["*Ghost of Tsushima*", "*Sekiro: Shadows Die Twice*", "*Nioh*"],
        "answer": "*Ghost of Tsushima*"
    },
    {
        "question": "What is the name of the robotic dinosaur in *Horizon Zero Dawn*?",
        "options": ["Thunderjaw", "Tallneck", "Watcher"],
        "answer": "Thunderjaw"
    },
    {
        "question": "Which PS1 game popularized the survival horror genre?",
        "options": ["*Silent Hill*", "*Resident Evil*", "*Parasite Eve*"],
        "answer": "*Resident Evil*"
    },
    {
        "question": "In *Uncharted 4*, what is Nathan Drake’s brother’s name?",
        "options": ["Sam", "Victor", "Rafe"],
        "answer": "Sam"
    },
    {
        "question": "Which Xbox-exclusive franchise stars a Spartan super-soldier?",
        "options": ["*Gears of War*", "*Halo*", "*Fable*"],
        "answer": "*Halo*"
    },
    {
        "question": "What is the name of the protagonist in *Gears of War*?",
        "options": ["Marcus Fenix", "Dominic Santiago", "Augustus Cole"],
        "answer": "Marcus Fenix"
    },
    {
        "question": "Which Xbox game features a post-apocalyptic Australia?",
        "options": ["*Mad Max*", "*Forza Horizon 3*", "*Rage 2*"],
        "answer": "*Forza Horizon 3*"
    },
    {
        "question": "In *Sea of Thieves*, what is the main objective?",
        "options": ["Hunt sea monsters", "Collect treasure", "Build a pirate empire"],
        "answer": "Collect treasure"
    },
    {
        "question": "Which studio developed *Ori and the Blind Forest*?",
        "options": ["Playground Games", "Moon Studios", "Ninja Theory"],
        "answer": "Moon Studios"
    },
    {
        "question": "What is the default name of the player character in *Minecraft*?",
        "options": ["Steve", "Alex", "Herobrine"],
        "answer": "Steve"
    },
    {
        "question": "Which PC game popularized the battle royale genre?",
        "options": ["*Fortnite*", "*PlayerUnknown’s Battlegrounds (PUBG)*", "*Apex Legends*"],
        "answer": "*PlayerUnknown’s Battlegrounds (PUBG)*"
    },
    {
        "question": "Who is regarded as the greatest *League of Legends* player in history?",
        "options": ["Chovy", "Faker", "Deft"],
        "answer": "Faker"
    },
    {
        "question": "Which game features a protagonist named Geralt of Rivia?",
        "options": ["*Dragon Age*", "*The Witcher*", "*Dark Souls*"],
        "answer": "*The Witcher*"
    },
    {
        "question": "What year did *World of Warcraft* launch?",
        "options": ["2002", "2004", "2006"],
        "answer": "2004"
    }
]