var errorMsg = document.getElementById("error")


function Card(suit, rank) {
  id = Math.random().toString(36).replace('0.', '').substr(0, 5)
  suits = [ 'SPADES', 'CLUBS', 'HEARTS', 'DIAMONDS' ]
  colors = [ 'BLACK', 'BLACK', 'RED', 'RED' ]
  suits_unicode_black = [ '♠', '♣', '♥', '♦' ]
  suits_unicode_white = [ '♤', '♧', '♡', '♢' ]
  suit_unicode_black = suits_unicode_black[suits.indexOf(suit)]
  suit_unicode_white = suits_unicode_white[suits.indexOf(suit)]
  ranks = [ 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' ]

  this.id = id
  this.suit = suit
  this.suit_unicode_black = suit_unicode_black
  this.suit_unicode_white = suit_unicode_white
  this.rank = rank
  this.formatting = "<div class='card'><div class='rank'>" + rank + "</div><div class='suit'>" + suit_unicode_black + "</div></div>"
  try {
    if (!suits.includes(suit)) throw "INVALID_SUIT (" + id + ")"
    if (!ranks.includes(rank)) throw "INVALID_RANK (" + id + ")"
  } catch(err) {
    errorMsg.innerHTML = err
  }
}

Card.prototype = {
  setSuit: function(suit) {
    this.suit = suit
  },
  getSuit: function() {
    return suit
  },
  setRank: function(rank) {
    this.rank = rank
  },
  getRank: function() {
    return rank
  }
}

var card = new Card('SPADES', 'J');
console.log("card: " + JSON.stringify(card));
document.write(card.formatting)
