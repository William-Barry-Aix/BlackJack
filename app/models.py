from django.contrib.auth.models import User
from django.db import models


class Player(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                default=None)

    def __str__(self):
        return '{}{}{}'.format(
            self.user.first_name if self.user is not None else '?',
            self.user.last_name if self.user is not None else '?',
            self.user.email if self.user is not None else '?',
        )


class Rank(models.Model):
    libelle = models.CharField(null=None,
                               default=None)

class Value(models.Model):
    rank = models.One

class Card(models.Model):
    rank = models.OneToManyField(Rank,
                            null=None,
                            default=None)

    value = models.OneToManyField(Value,
                                  null=None,
                                  default=None)

    suit = models.TextField(Suit,
                            null=None,
                            default=None)

    isVisible = models.BooleanField(null=None,
                                    default=False)

    def __str__(self):
        return self.suit + self.rank


class Hand(models.Model):
    cards = models.OneToManyField(Card,
                                  on_delete=models.CASCADE,
                                  default=None)


class Deck(models.Model):
    cards = models.OneToManyField(Card,
                                  on_delete=models.CASCADE,
                                  default=None)


class Session(models.Model):
    bet = models.IntegerField(null=None,
                              default=None)

    place = models.IntegerField(null=None,
                                default=None)

    insurance = models.IntegerField(null=None,
                                    default=None)

    # TODO: role
    # TODO: game
    # TODO: player
    # TODO: hand
