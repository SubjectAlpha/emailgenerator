'''
Notice: Currently this will generate around 36,205,000 possible emails if all flags are enabled
'''
import os, sys

STORAGE_PATH = f"{os.getcwd()}/emails/"
GENERATED_FILE = f"{STORAGE_PATH}generated_emails.txt"
CHUNK_SIZE = 20000
USE_DEFAULT_HOSTS = True
USER_HOSTS = ""
INCLUDE_YEARS = False
INCLUDE_NUMBERS = False

def get_names():
    first_names = ["james", "robert", "michael", "david", "william", "richard", 
        "dick", "joseph", "joe", "thomas", "tom", "charles", "chuck", "christopher", "chris",
        "matthew", "matt", "anthony", "tony", "mark", "donald", "don", "steven", "steve", "paul",
        "andrew", "drew", "joshua", "josh", "kenneth", "ken", "kenny", "kevin", "brian", "george",
        "timothy", "tim", "ronald", "ron", "edward", "ed", "jason", "jeffrey", "jeff", "ryan", "jacob", "jake",
        "gary", "nicholas", "nick", "eric", "erik", "jonathan", "jon", "john", "stephen", "larry", "justin", "scott",
        "brandon", "benjamin", "ben", "samuel", "sam", "gregory", "greg", "alexander", "alex", "frank", "patrick", "rick",
        "raymond", "ray", "jack", "jackson", "dennis", "jerry", "tyler", "aaron", "jose", "adam", "nathan", "nate", "henry",
        "douglas", "doug", "zachary", "zach", "zack", "peter", "pete", "kyle", "ethan", "walter", "noah", "jeremy",
        "christian", "keith", "roger", "terry", "gerald", "harold", "sean", "shawn", "austin", "carl", "arthur",
        "lawrence", "dylan", "jesse", "jesse", "jordan", "bryan", "billy", "bruce", "gabriel", "gabe", "logan",
        "albert", "al", "willie", "willy", "alan", "juan", "wayne", "elijah", "eli", "randy", "roy", "vincent", "vince",
        "ralph", "eugene", "russell", "russ", "bobby", "mason", "philip", "phil", "phillip", "louis", "lou", "louie", "lewis",
        "logan", "devin", "dorian",
        "mary", "patricia", "pat", "pattie", "jennifer", "jenny", "jen", "linda", "elizabeth", "liz", "beth", "barbara", "barb",
        "susan", "sue", "jessica", "jess", "sarah", "sara", "karen", "lisa", "nancy", "betty", "margaret", "sandra", "ashley",
        "kimberly", "emily", "donna", "michelle", "carol", "amanda", "dorothy", "melissa", "deborah", "stephanie", "rebecca",
        "sharon", "laura", "cynthia", "kathleen", "amy", "angela", "shirley", "anna", "brenda", "pamela", "emma", "nicole",
        "helen", "samantha", "sam", "katherine", "kat", "christine", "debra", "rachel", "carolyn", "janet", "catherine",
        "maria", "heather", "diane", "ruth", "julie", "olivia", "joyce", "virginia", "victoria", "kelly", "lauren",
        "christina", "joan", "evelyn", "judith", "megan", "andrea", "cheryl", "hannah", "jacqueline", "jackie", "martha",
        "gloria", "teresa", "ann", "anne", "madison", "frances", "kathryn", "janice", "jean", "abigail", "abby",
        "alice", "julia", "judy", "sophia", "sophie", "grace", "denise", "amber", "doris", "marilyn", "danielle",
        "beverly", "bev", "isabelle", "belle", "theresa", "diana", "natalie", "brittany", "charlotte", "marie",
        "kayla", "alexis", "lori"] #https://www.ssa.gov/oact/babynames/decades/century.html
    
    last_names = ["wang", "smith", "devi", "ivanov", "kim", "ali", "garcia", "muller", "silva", "dasilva", "mohammed",
        "tesfaye", "nguyen", "ilunga", "gonzalez", "deng", "rodriguez", "moyo", "hansen", "zhang", "johnson", "williams",
        "brown", "jones", "anderson", "hernandez", "lopez", "miller", "chavez", "davis", "wilson", "thomas", "taylor",
        "moore", "jackson", "martin", "lee", "perez", "thompson", "white", "haris", "sanchez", "clark", "ramirez",
        "lewis", "robinson", "walker", "young", "allen", "king", "right", "scott", "torres", "hill", "flores", "green",
        "adams", "nelson", "baker", "hall", "rivera", "campbell", "mitchell", "carter", "roberts", "gomez", "phillips",
        "evans", "turner", "diaz", "parker", "cruz", "edwards", "collins", "reyes", "stewart", "morris", "morales",
        "murphy", "cook", "rogers", "gutierrez", "ortiz", "morgan", "cooper", "peterson", "bailey", "reed", "kelly",
        "howard", "ramos", "kim", "cox", "ward", "richardson", "watson", "brooks", "chavez", "wood", "james",
        "bennet", "grey", "mendoza", "ruiz", "hughes", "price", "alvarez", "catillo", "sanders", "patel", "myers", 
        "ross", "foster", "jimenez"] #https://www.thoughtco.com/most-common-us-surnames-1422656
    
    return [(a, b) for a in first_names for b in last_names]

def add_arbitrary_numbers(name_pair):
    possible_combinations = [f"{name_pair[0]}{name_pair[1]}", f"{name_pair[0]}.{name_pair[1]}"]

    if INCLUDE_NUMBERS:
        #cover smaller numbers like sports numbers and abbreviated years
        for i in range(0,100):
            possible_combinations.append(f"{name_pair[0]}.{name_pair[1]}{i}")
            possible_combinations.append(f"{name_pair[0]}{name_pair[1]}{i}")
    
    if INCLUDE_YEARS:
        #cover from 1950-2050 for birth years and grad years
        for i in range(1950, 2050):
            possible_combinations.append(f"{name_pair[0]}.{name_pair[1]}{i}")
            possible_combinations.append(f"{name_pair[0]}{name_pair[1]}{i}")

    return possible_combinations

def write_file(data, chunk_count):
    filename = f"{STORAGE_PATH}email_list_{chunk_count}.txt"
    try:
        with open(filename, "w") as nf:
            nf.writelines(data)
    except:
        print("There was a problem writing to the file")

def disperse_emails():
    chunk_count = 1
    line_count = 0

    if os.path.exists(GENERATED_FILE):
        with open(GENERATED_FILE, "r") as f:
            buffered_string = ""
            for line in f.readlines():
                if line_count < int(CHUNK_SIZE):
                    buffered_string += line
                    line_count += 1
                else:
                    write_file(buffered_string, chunk_count)
                    buffered_string = ""
                    line_count = 0
                    chunk_count += 1
    else:
        print("Email list file not found. Please use -g flag to generate a new one.")

def generate_email_list():
    default_email_hosts = ["gmail.com", "outlook.com", "hotmail.com"]
    all_possible_names = get_names()

    if not os.path.exists(STORAGE_PATH):
        os.mkdir(STORAGE_PATH)

    with open(GENERATED_FILE, "w") as f:
        for names in all_possible_names:
            bastardized_names = add_arbitrary_numbers(names)
            for name in bastardized_names:
                if USE_DEFAULT_HOSTS:
                    for host in default_email_hosts:
                        f.write(f"{name}@{host}\n")
                else:
                    hosts = USER_HOSTS.split(',')
                    for host in hosts:
                        f.write(f"{name}@{host}\n")

def main():
    if len(sys.argv) > 1:
        help_flag = "-h"
        host_flag = "-d"
        generate_flag = "-g"
        size_flag = "-s"
        years_flag = "-y"
        numbers_flag = "-n"
        output_flag = "-o"

        help_messages = [
            f"{help_flag} for help",
            f"{generate_flag} to generate a new bulk list",
            f"{size_flag} to set chunk size DEFAULT:20000",
            f"{host_flag} to enter a cvs list of desired email hosts DEFAULT: gmail.com, hotmail.com, outlook.com",
            f"{numbers_flag} to include numbers 0-100 to cover common sports numbers and year abbreviations that may are likely to be included in email",
            f"{years_flag} to include years 1950-2050 for common graduation/birth years in email"
        ]
        
        if help_flag in sys.argv:
            for msg in help_messages:
                print(msg)
            return

        if host_flag in sys.argv:
            if not generate_flag in sys.argv:
                print(f"You must use the {generate_flag} flag to use the {host_flag} flag")
                exit()

            USE_DEFAULT_HOSTS = False
            USER_HOSTS = sys.argv[sys.argv.index(host_flag) + 1]

        if output_flag in sys.argv:
            output_dir = sys.argv[sys.argv.index(output_flag) + 1]
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)
            STORAGE_PATH = output_dir
            GENERATED_FILE = f"{STORAGE_PATH}generated_emails.txt"

        if size_flag in sys.argv:
            CHUNK_SIZE = sys.argv[sys.argv.index(size_flag) + 1]

        if numbers_flag in sys.argv:
            INCLUDE_NUMBERS = True

        if years_flag in sys.argv:
            INCLUDE_YEARS = True

        if generate_flag in sys.argv:
            generate_email_list()
    
        disperse_emails()
