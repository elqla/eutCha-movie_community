from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user = super().save_user(request, user, form, False)
        nickname = data.get('nickname')
        if nickname:
            user.nickname = nickname
        picture = data.get('picture')
        if picture:
            user.picture = picture
        user.save()
        return user