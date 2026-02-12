import random


def set_up_list(rng):
    return list(range(1,rng+1))

def get_random_element(tickets):
    return random.choice(tickets) 

def remove_ticket(tickets, winning_number):
    tickets.remove(winning_number)
    return tickets       

def main():
    rng = 20
    number_raffles = 0
    number_prizes_won = 0
    for raffle in range(1_000_000):
        tickets = set_up_list(rng)
        number_raffles += 1
        #print(f"{tickets = }")
        ticket_number = random.randint(1,rng)
        for prize_number in range(3):
            winning_number = get_random_element(tickets)
           # print(f"{tickets = }")
            tickets = remove_ticket(tickets, winning_number)
            number_prizes_won += ticket_number == winning_number       
    odds_of_winning = number_prizes_won / number_raffles
    print(f"{odds_of_winning = }")
    print(f"{(1/(rng))+(1/(rng-1))+(1/(rng-2)) = }")       


if __name__ == "__main__":
    main()