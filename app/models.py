from django.conf import settings
from django.db import models

class Message(models.Model):
    """Un message laissé depuis le formulaire de contact (app/templates/message.html)."""

    titre = models.CharField("Titre", max_length=150)
    contenu = models.TextField("Message")
    auteur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="messages",
        verbose_name="Auteur",
    )
    date_envoi = models.DateTimeField("Envoyé le", auto_now_add=True)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ["-date_envoi"]

    def __str__(self):
        return f"{self.titre} ({self.date_envoi:%d/%m/%Y %H:%M})"

