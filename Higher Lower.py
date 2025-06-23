import random

data=[
  {
    "name": "Taylor Swift",
    "follower_count": 298,
    "description": "Singer-songwriter",
    "country": "United States"
  },
  {
    "name": "Ed Sheeran",
    "follower_count": 170,
    "description": "Singer-songwriter",
    "country": "United Kingdom"
  },
  {
    "name": "Beyoncé",
    "follower_count": 315,
    "description": "Singer, songwriter, and businesswoman",
    "country": "United States"
  },
  {
    "name": "Bad Bunny",
    "follower_count": 95,
    "description": "Rapper and singer",
    "country": "Puerto Rico"
  },
  {
    "name": "Billie Eilish",
    "follower_count": 130,
    "description": "Singer-songwriter",
    "country": "United States"
  },
  {
    "name": "Drake",
    "follower_count": 145,
    "description": "Rapper and singer",
    "country": "Canada"
  },
  {
    "name": "Rihanna",
    "follower_count": 160,
    "description": "Singer, businesswoman",
    "country": "Barbados"
  },
  {
    "name": "Justin Bieber",
    "follower_count": 290,
    "description": "Singer-songwriter",
    "country": "Canada"
  },
  {
    "name": "Adele",
    "follower_count": 55,
    "description": "Singer-songwriter",
    "country": "United Kingdom"
  },
  {
    "name": "The Weeknd",
    "follower_count": 115,
    "description": "Singer-songwriter",
    "country": "Canada"
  },
  {
    "name": "Dua Lipa",
    "follower_count": 90,
    "description": "Singer-songwriter",
    "country": "United Kingdom"
  },
  {
    "name": "Ariana Grande",
    "follower_count": 380,
    "description": "Singer and actress",
    "country": "United States"
  },
  {
    "name": "Shawn Mendes",
    "follower_count": 75,
    "description": "Singer-songwriter",
    "country": "Canada"
  },
  {
    "name": "Camila Cabello",
    "follower_count": 65,
    "description": "Singer-songwriter",
    "country": "Cuba"
  },
  {
    "name": "Post Malone",
    "follower_count": 45,
    "description": "Rapper and singer",
    "country": "United States"
  },
  {
    "name": "Cardi B",
    "follower_count": 160,
    "description": "Rapper and songwriter",
    "country": "United States"
  },
  {
    "name": "Doja Cat",
    "follower_count": 40,
    "description": "Rapper and singer",
    "country": "United States"
  },
  {
    "name": "Harry Styles",
    "follower_count": 60,
    "description": "Singer-songwriter and actor",
    "country": "United Kingdom"
  },
  {
    "name": "Lady Gaga",
    "follower_count": 60,
    "description": "Singer, songwriter, and actress",
    "country": "United States"
  },
  {
    "name": "Katy Perry",
    "follower_count": 200,
    "description": "Singer-songwriter",
    "country": "United States"
  },
  {
    "name": "Snoop Dogg",
    "follower_count": 80,
    "description": "Rapper and actor",
    "country": "United States"
  },
  {
    "name": "Nicki Minaj",
    "follower_count": 230,
    "description": "Rapper and songwriter",
    "country": "Trinidad and Tobago"
  },
  {
    "name": "Selena Gomez",
    "follower_count": 420,
    "description": "Singer, actress, and producer",
    "country": "United States"
  },
  {
    "name": "Rosalía",
    "follower_count": 25,
    "description": "Singer-songwriter",
    "country": "Spain"
  },
  {
    "name": "Coldplay",
    "follower_count": 30,
    "description": "Band",
    "country": "United Kingdom"
  },
  {
    "name": "Bruno Mars",
    "follower_count": 35,
    "description": "Singer-songwriter",
    "country": "United States"
  },
  {
    "name": "Miley Cyrus",
    "follower_count": 210,
    "description": "Singer, songwriter, and actress",
    "country": "United States"
  },
  {
    "name": "Shakira",
    "follower_count": 95,
    "description": "Singer-songwriter",
    "country": "Colombia"
  },
  {
    "name": "Sam Smith",
    "follower_count": 15,
    "description": "Singer-songwriter",
    "country": "United Kingdom"
  },
  {
    "name": "Eminem",
    "follower_count": 65,
    "description": "Rapper and producer",
    "country": "United States"
  }
]

def format_data(account):
    account_name=account['name']
    account_des=account['description']
    account_foll=account['follower_count']
    account_country=account['country']
    print(f"{account_name}, a {account_des}, from {account_country}")

def check_answer(user_guess,a_foll,b_foll):
    if a_foll>b_foll:
        return user_guess=='A'
    else:
        return user_guess=='B'
game=True
account_b=random.choice(data)
score=0

while game:

    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)

    format_data(account_a)
    print('VS')
    format_data(account_b)
    guess=input('Compare A against B (A or B): ').upper()

    a_foll_count=account_a["follower_count"]
    b_foll_count=account_b["follower_count"]

    is_correct=check_answer(guess,a_foll_count,b_foll_count)
    if is_correct:
        score+=1
        print('You are right! Current score' ,score)
    else:
        print('Sorry! Thats wrong. Final Score ',score)
        game=False

    


























