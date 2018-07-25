import random
import os
import pygame
from turtle import *
import time


HANGMAN = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def choose_word():
    return random.sample(WORDS, 1)  # chooses a word to play with


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")  # clears screen


def hangman_1():
    color('black')
    pensize(5)
    speed(5)
    fd(150)
    lt(180)
    fd(100)
    rt(90)
    fd(300)
    rt(90)
    fd(75)
    rt(90)
    fd(50)


def hangman_2():
    rt(90)
    circle(25)
    return None

def hangman_3():
    circle(25, 180)
    rt(90)
    fd(25)
    rt(90)
    fd(50)
    rt(180)
    fd(100)
    rt(180)
    fd(50)
    lt(90)
    fd(25)

def hangman_4():
    rt(180)
    fd(25)
    lt(90)
    fd(50)
    lt(65)
    fd(25)
    lt(180)
    fd(50)

def hangman_5():
    lt(180)
    fd(25)
    lt(115)
    fd(100)
    lt(120)
    fd(25)
    rt(180)
    fd(50)

def hangman_6():
    rt(180)
    fd(25)
    lt(60)
    fd(50)
    lt(90)
    fd(55)


def hangman_7():
    fd(20)


def hangman_8():
    rt(45)
    fd(50)


def hangman_9():
    fd(25)


def hangman_10():
    rt(180)
    fd(75)
    rt(90)
    fd(50)


def hangman_11():
    fd(25)
    print('You may now close the turtle. ')
    done()




def game_loop():
    fd(1)  # You must initialize turtle before pygame or else you will get an error
    pygame.init()
    hangman = pygame.mixer.Sound("./media/HangmanWav1.wav")
    hangman.play()
    input("Press 'Enter' to play Hangman!  ")  # starts game
    pygame.init()
    hangman = pygame.mixer.Sound("./media/RUN.wav")
    hangman.play()
    clear_screen()  # clears screen
    words = choose_word()  # chooses a word
    word = words[0]  # converts word into a str from list
    word_guessed = [] # word in '-' and letter form
    for _ in word:
        word_guessed.append("-")  # create an unguessed, blank version of the word
    joined_word = None  # joins the words in the list word_guessed
    tries = 10  # how many times you are aloud to fail
    guessed_letters = []  # list of all letters guessed
    hangman_1()  # Draws hangman
    while tries != 0 and "-" in word_guessed:
        print("\nYou have {} attempts remaining".format(tries))
        pygame.init()
        hangman = pygame.mixer.Sound("./media/Tries.wav")
        hangman.play()
        time.sleep(3)
        strs = ''.join(word_guessed)
        print(strs)
        try:
            pygame.init()
            hangman = pygame.mixer.Sound("./media/Select.wav")
            hangman.play()
            time.sleep(4)
            player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()

        except ValueError:  # check valid input
            pygame.init()
            hangman = pygame.mixer.Sound("./media/ValidInput.wav")
            hangman.play()
            print("That is not valid input. Please try again.")
            time.sleep(3)
            continue

        else:
            if not player_guess.isalpha():  # check the input is a letter. Also checks an input has been made.
                pygame.init()
                hangman = pygame.mixer.Sound("./media/NotLetter.wav")
                hangman.play()
                print("That is not a letter. Please try again.")
                time.sleep(4.5)
                continue
            elif len(player_guess) > 1:  # check the input is only one letter
                pygame.init()
                hangman = pygame.mixer.Sound("./media/MoreLetter.wav")
                hangman.play()
                print("That is more than one letter. Please try again.")
                time.sleep(3)
                continue
            elif player_guess in guessed_letters:  # check it letter hasn't been guessed already
                pygame.init()
                hangman = pygame.mixer.Sound("./media/Guessed.wav")
                hangman.play()
                print("You have already guessed that letter. Please try again.")
                time.sleep(5)
                continue
            else:
                pass

        guessed_letters.append(player_guess)

        for letter in range(len(word)):
            if player_guess.lower() == (word[letter].lower()):
                word_guessed[letter] = player_guess  # replace all letters in the chosen word that match the players guess
                pygame.init()
                drums = pygame.mixer.Sound("./media/drum_roll_y.wav")
                drums.play()


        if player_guess.lower() not in word.lower():
            tries -= 1
            pygame.init()
            gasp = pygame.mixer.Sound("./media/gasp_x.wav")
            gasp.play()
            if HANGMAN[(len(HANGMAN) - 1) - tries] == HANGMAN[1]:
                hangman_2()
            elif HANGMAN[(len(HANGMAN) - 1) - tries] == HANGMAN[2]:
                hangman_3()
            elif HANGMAN[(len(HANGMAN) - 1) - tries] == HANGMAN[3]:
                hangman_4()
            elif HANGMAN[(len(HANGMAN) - 1) - tries] == HANGMAN[4]:
                hangman_5()
            elif HANGMAN[(len(HANGMAN) - 1) - tries] == HANGMAN[5]:
                hangman_6()
            elif HANGMAN[(len(HANGMAN) - 1) - tries] == HANGMAN[6]:
                hangman_7()
            elif HANGMAN[(len(HANGMAN) - 1) - tries] == HANGMAN[7]:
                hangman_8()
            elif HANGMAN[(len(HANGMAN) - 1) - tries] == HANGMAN[8]:
                hangman_9()
            elif HANGMAN[(len(HANGMAN) - 1) - tries] == HANGMAN[9]:
                hangman_10()
            elif HANGMAN[(len(HANGMAN) - 1) - tries] == HANGMAN[10]:
                hangman_11()

    if "-" not in word_guessed:  # no blanks remaining
        pygame.init()
        hangman = pygame.mixer.Sound("./media/Congrats.wav")
        hangman.play()
        print("\nCongratulations! {} was the word!".format(word))
        pygame.init()
        cymbal = pygame.mixer.Sound("./media/applause3.wav")
        cymbal.play()
        ball = pygame.mixer.Sound("./media/woow_x.wav")
        ball.play()
        sphere = pygame.mixer.Sound("./media/Victory.wav")
        sphere.play()
        reset()
    else:  # loop must have ended because attempts reached 0
        pygame.init()
        hangman = pygame.mixer.Sound("./media/Unlucky.wav")
        hangman.play()
        print("\nUnlucky! The word was {}.".format(word))
        pygame.init()
        hangman = pygame.mixer.Sound("./media/fail-trombone-02.wav")
        hangman.play()


WORDS = ['Awkward', 'Bagpipes', 'Banjo', 'Bungler', 'Croquet', 'Crypt', 'Dwarves', 'Fervid', 'Fishhook', 'Fjord',
         'Gazebo',
         'Gypsy', 'Haiku', 'Haphazard', 'Hyphen', 'Ivory', 'Jazzy', 'Jiffy', 'Jinx', 'Jukebox', 'Kayak', 'Kiosk',
         'Klutz', 'Memento', 'Mystify', 'Numbskull', 'Ostracize', 'Oxygen', 'Pajama', 'Phlegm', 'Pixel', 'Polka',
         'Quad', 'Quip', 'Rhythmic', 'Rogue', 'Sphinx', 'Squawk', 'Swivel', 'Toady', 'Twelfth', 'Unzip', 'Waxy',
         'Wildebeest', 'Yacht',
         'Zealous', 'Zigzag', 'Zippy', 'Zombie', 'TheZombieHorde', "hangman", "chairs", "backpack", "bodywash",
         "clothing", "computer", "python", "program", "glasses", "sweatshirt", "sweatpants", "mattress", "friends",
         "clocks", "biology", "algebra", "suitcase", "knives", "ninjas", "shampoo", "python", "jumble", "easy",
         "difficult", "answer",  "xylophone"]
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret ' \
        'fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon ' \
        'python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad ' \
        'trout ' \
        'turkey turtle weasel whale wolf wombat zebra'\
        '''they
with
not
that
on
she
as
at
by
this
we
you
do
from
or
an
but
which
would
say
all
one
will
there
that
who
make
when
if
man
can
what
no
go
time
up
into
year
other
out
could
some
new
that
know
these
take
see
get
come
only
two
any
state
give
now
may
than
then
also
find
as
way
day
first
even
use
first
more
many
must
think
such
like
should
so
through
more
people
those
over
where
just
seem
life
good
each
become
back
world
here
between
both
thing
hand
own
very
tell
how
down
work
because
school
same
under
never
house
after
great
old
still
leave
well
want
three
another
call
against
last
number
show
most
child
one
feel
part
ask
place
few
about
might
turn
long
while
so
small
problem
during
word
live
system
area
write
again
follow
begin
Mister
fact
without
program
eye
there
country
Mrs.
himself
city
stand
provide
so
much
work
group
hold
too
case
most
off
line
on
night
for
course
put
point
government
something
head
American
let
away
always
church
bring
high
out
war
since
every
unite
room
class
keep
before
need
than
however
try
though
little
use
woman
end
boy
hear
upon
company
service
large
side
order
run
car
week
why
water
social
move
president
business
figure
start
face
several
mean
set
toward
appear
over
question
among
value
young
nothing
family
within
serve
member
once
form
law
matter
often
help
continue
John
name
before
only
four
power
general
per
believe
after
possible
body
development
foot
force
increase
pay
important
type
meet
nation
play
cost
today
expect
kind
door
street
home
big
reach
girl
require
result
month
hour
lead
period
office
later
white
reason
field
sit
such
example
home
job
action
consider
develop
college
rate
around
history
national
pass
next
like
experience
position
moment
God
mind
public
best
study
happen
sense
local
interest
walk
perhaps
method
idea
grow
town
money
until
read
book
policy
effort
person
add
ever
remain
themselves
although
talk
five
speak
probably
other
first
almost
effect
society
whole
condition
second
across
little
level
center
student
light
art
shall
send
determine
wife
material
least
yet
voice
community
party
ago
air
carry
wait
mother
tax
build
board
lose
too
already
involve
Doctor
human
fall
available
thus
all
learn
draw
anything
process
minute
understand
table
special
federal
section
death
much
difference
break
remember
century
control
far
economic
open
ground
stop
stage
full
certain
department
whether
change
father
better
different
piece
indicate
picture
place
really
quite
receive
music
itself
road
university
information
behind
enough
situation
common
purpose
include
free
letter
produce
paper
apply
TRUE
together
mile
arm
report
cut
land
early
evidence
much
usually
issue
present
real
age
plan
peace
bear
necessary
strong
drive
open
step
record
less
horse
spend
friend
right
enter
six
wall
short
watch
officer
son
really
statement
morning
unit
heart
more
all
modern
therefore
space
greater
fire
no
back
long
along
court
above
story
alone
right
personal
suggest
river
able
nor
secretary
less
operation
allow
sometimes
organization
major
clear
everything
sure
half
plant
reduce
county
describe
plan
wear
subject
cent
report
right
seek
datum
decide
source
food
else
nature
committee
accept
stay
event
district
volume
opportunity
station
close
equipment
need
basic
including
around
explain
third
trial
rise
die
offer
except
research
note
defense
cover
contain
enough
private
black
because
feeling
south
down
love
cause
purpose
raise
represent
suppose
change
buy
movement
finally
factor
act
amount
product
hope
military
club
science
prepare
leader
million
almost
better
difficult
reaction
test
temperature
complete
decision
drop
fund
up
market
assume
dead
attention
price
quality
game
sort
dark
color
lie
simply
political
fight
building
pressure
husband
realize
establish
medical
since
recent
obtain
choose
recognize
window
front
growth
study
permit
image
along
soon
exist
direction
basis
concern
simple
win
character
administration
machine
ten
earth
either
term
technique
religious
God
teacher
principle
production
present
sale
form
anyone
increase
evening
association
size
actually
disagree
meeting
kill
instead
range
fill
army
labor
hair
floor
face
cell
rule
international
wish
relation
trouble
thought
writer
performance
population
create
Congress
result
lot
pull
stock
especially
yes
leach
language
maintain
foreign
plane
act
pattern
agree
dollar
meaning
element
view
off
fine
list
religion
beyond
opinion
design
rather
natural
procedure
central
west
occur
tree
certainly
various
individual
low
summer
support
near
operate
literature
sound
project
southern
answer
normal
patient
late
industrial
return
well
attitude
knowledge
catch
poet
role
achieve
length
similar
limit
point
England
return
fail
hard
hospital
red
yet
throw
relate
addition
western
manner
inch
single
public
throughout
hundred
hot
prove
support
join
higher
ready
train
distance
how
end
spring
hit
bad
function
hotel
police
maybe
no
former
physical
farm
before
prevent
charge
detail
moral
directly
treatment
remove
entire
possibility
far
set
radio
loss
individual
sign
lay
merely
scene
corner
responsibility
Christian
apparently
measure
mean
likely
indeed
gun
eat
couple
ride
but
larger
truth
state
practice
suddenly
fear
play
lady
season
cold
pick
chance
express
base
institution
hang
until
theory
worker
mention
design
beautiful
agreement
answer
extend
leg
rest
vary
Brown
smile
respect
brother
analysis
future
right
feed
discussion
total
item
influence
freedom
conference
bill
commission
claim
final
strength
shoot
difficulty
success
region
structure
discuss
effective
mark
hall
dog
glass
relationship
choice
hill
discover
recently
model
concern
date
ship
American
easy
as
listen
particular
enjoy
ball
general
technical
force
governor
announce
nearly
firm
experiment
pool
serious
aid
longer
visit
strike
square
trip
wonder
director
latter
love
improve
Europe
enemy
according
care
mouth
one
deal
edge
object
account
slowly
demand
sell
afternoon
suffer
oil
little
press
early
wide
that
contribute
instance
compare
poem
direct
citizen
herself
audience
U.S.
election
fix
park
bar
immediately
cause
division
English
agency
French
rather
boat
faith
top
artist
page
name
saint
facility
finger
manager
gas
series
supply
tooth
weapon
approach
bed
specific
save
marry
none
parent
myself
attend
will
employee
authority
publish
settle
marriage
however
fiscal
look
interact
democratic
generally
select
kid
captain
importance
march
forget
bank
finish
affair
oh
animal
hope'''.split()

WORDS.extend(words)



game_loop()

