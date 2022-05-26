# 파이널프로젝트 

### 05.22.

movies의 urls.py, views.py를 작성했다.

##### eutgorithm

- DB에서 알고리즘을 적용해 영화 5개를 응답해주는 요청 URL을 `eut/`으로 만들었다.

- export_genre를 만들어, 알고리즘을 적용했다.
  - 요청을 보낸 user의 정보 중, like와 dislike를 누른 영화들을 역참조로 불러오고, 그 영화들의 genres를 모두 순회하여, like를 누른 영화의 장르들에는 +1점, dislike를 누른 영화의 장르들에는 -1점을 부여하였다.
  - 모두 합산한 점수를 토대로, 가장 높은 점수가 가장 좋아하는 장르이며, 가장 낮은 점수가 가장 싫어하는 장르라고 판단했다.
  - 가장 좋아하는 장르가 포함되고, 가장 싫어하는 장르가 없는 영화 5개를 추천하도록 알고리즘을 구현했다.

##### popular

- DB의 영화 중 popularity가 가장 높은 5개를 응답하는 요청 URL을 `popular/`로 만들었다.

##### recent

- DB의 영화 중 release_date가 가장 큰 5개를 응답하는 요청 URL을 `recent/`로 만들었다.

##### new, movie_detail, like, dislike

- movie를 만들거나, 수정, 삭제하는 행위는 user중 staff권한을 가진 user만 할 수 있도록 제한하는 조건문을 포함하도록 만들었다.

```python
if request.user.is_staff
```

- 영화의 like, dislike는 POST요청으로만 가능하도록 했으며, 토글 가능하도록 했다.
  - 영화의 like를 누르면 dislike가 불가능하게, dislike를 누르면 like가 불가능하도록 해야할 것 같다.



### 05.23

accounts에서 프로필에 관련된 응답을 할 수 있도록 대부분 수정했다.

##### models.py

- 프로필 사진을 DB에 저장할 수 있도록, picture 필드를 추가했다.
- 이를 위해 pillow, imagekit 라이브러리를 설치했다.



### 05.24

- 해야할 일
  - back에서 검색어가 포함된 영화 객체를 응답하는 URL 만들기
  - 글 쓸때, movie에 검색어를 입력하면, 요청을 계속 보내줘서(input event?) 아래에 영화 객체를 선택할 수 있도록 하기./



### 05.25

- signup이 안된다...
  - nickname과 picture는 allauth로 업로드를 못하나?
- 해결방안
  - django에서 CustomRegisterSerializer와 CustomAccountAdapter를 만들어주고, settings.py에 등록해주면 된다.

```python
# accounts/adapters.py

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
```

```python
# accounts/serializers.py

from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=10)
    picture = serializers.ImageField(use_url=True)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['nickname'] = self.validated_data.get('nickname', '')
        data_dict['picture'] = self.validated_data.get('picture', '')
        return data_dict
```

```python
# settings.py

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer',
}

ACCOUNT_ADAPTER = 'accounts.adapters.CustomAccountAdapter'
```

