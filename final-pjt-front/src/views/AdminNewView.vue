<template>
  <div class="container" style="margin-top: 100px;">
    <h1>newMovie</h1>
    <b-form @submit.prevent="newMovie(credentials)" align="left">
      <b-form-group label-for="title" label="제목">
        <b-form-input v-model="credentials.title" id="title" placeholder="제목" type="text" required>
        </b-form-input>
      </b-form-group>
      <br>
      <b-form-group label-for="overview" label="시놉시스">
        <b-form-input v-model="credentials.overview" id="overview" placeholder="시놉시스" type="text" required>
        </b-form-input>
      </b-form-group>
      <br>
      <b-form-group label-for="credits" label="출연 배우들">
        <b-form-input v-model="credentials.credits" id="credits" placeholder="출연 배우들" type="text" required>
        </b-form-input>
      </b-form-group>
      <br>
      <b-form-group label-for="genres" label="장르">
        <b-form-select v-model="credentials.genres" :options="options" multiple :select-size="10" id="genres" type="text" required>
        </b-form-select>
        <div>선택한 장르: {{ credentials.genres }}</div>
      </b-form-group>
      <br>
      <b-form-group label-for="release_date" label="개봉일">
        <b-form-input v-model="credentials.release_date" id="release_date" placeholder="개봉일" type="text" required>
        </b-form-input>
      </b-form-group>
      <br>
      <b-form-group label-for="popularity" label="유명도">
        <b-form-input v-model="credentials.popularity" id="popularity" type="number" required>
        </b-form-input>
      </b-form-group>
      <br>
      <b-form-group label-for="movie_id" label="영화 ID">
        <b-form-input v-model="credentials.movie_id" id="movie_id" type="number" required>
        </b-form-input>
      </b-form-group>
      <br>
      <b-form-group label-for="poster_url" label="포스터 URL">
        <b-form-input v-model="credentials.poster_url" id="poster_url" placeholder="/asdf.jpg" type="text" required>
        </b-form-input>
      </b-form-group>
      <b-button type="submit" variant="dark">영화 등록하기</b-button>
    </b-form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'AdminNewView',
  data() {
    return {
      credentials: {
        title: '',
        overview: '',
        credits: '',
        genres: [],
        release_date: '',
        popularity: 0,
        movie_id: 0,
        poster_url: ''
      },
      options: [
        { value: 12, text: '모험' },
        { value: 14, text: '판타지' },
        { value: 16, text: '애니메이션' },
        { value: 18, text: '드라마' },
        { value: 27, text: '공포' },
        { value: 28, text: '액션' },
        { value: 35, text: '코미디' },
        { value: 36, text: '역사' },
        { value: 37, text: '서부' },
        { value: 53, text: '스릴러' },
        { value: 80, text: '범죄' },
        { value: 99, text: '다큐멘터리' },
        { value: 878, text: 'SF' },
        { value: 9648, text: '미스터리' },
        { value: 10402, text: '음악' },
        { value: 10749, text: '로맨스' },
        { value: 10751, text: '가족' },
        { value: 10752, text: '전쟁' },
        { value: 10770, text: 'TV 영화' },
      ]
    }
  },
  methods: {
    ...mapActions(['newMovie'])
  }
}
</script>

<style>

</style>