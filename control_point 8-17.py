counter = 0
mystring = """If you like to gamble, I tell you I'm your man
You win some, lose some, all the same to me

The pleasure is to play, makes no difference what you say
I don't share your greed, the only card I need is the Ace of Spades
The Ace of Spades

Playing for the high one, dancing with the devil
Going with the flow, it's all a game to me

Seven or eleven, snake eyes watching you
Double up or quit, double stake or split, the Ace of Spades
The Ace of Spades

You know I'm born to lose, and gambling's for fools
But that's the way I like it baby
I don't wanna live for ever
And don't forget the joker!

Pushing up the ante, I know you gotta see me
Read 'em and weep, the dead man's hand again

I see it in your eyes, take one look and die
The only thing you see, you know it's gonna be the Ace of Spades
The Ace of Spades."""

for letter in mystring:
    if letter.isupper():
        counter += 1 
        
print(counter)
