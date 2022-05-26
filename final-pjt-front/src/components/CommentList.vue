<template>
  <div class="d-flex comment-item">
    <div>
      <span class="comment-user">{{ comment.user.nickname || comment.user.username }}</span>
      <span class="comment-content">{{ comment.content }}</span>
    </div>
    <div class="commentcud d-flex">
      <div>
      <div class="">create: {{$moment(comment.created_at).calendar()}}</div>
      <div class="">update: {{$moment(comment.updated_at).calendar()}}</div>
      </div>
      <div v-if="currentUser.username===comment.user.username" class="deleteC">
      <b-button @click="deleteComment({articlePk, commentPk})" pill variant="danger">삭제</b-button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'CommentList',
  props: {
    comment: Object,
  },
  computed:{
    ...mapGetters(['currentUser',]),
    articlePk() {
      return this.comment.article
    },
    commentPk (){
      return this.comment.id
    }
  },
  methods:{
    ...mapActions(['deleteComment',]),
  }
}
</script>

<style>

.comment-item {
  margin-bottom: 5px;
  padding: 1rem;
  border-style: solid;
  border-width: 1px;
  border-radius: 1rem;
  font-family: 'Gowun Dodum', sans-serif;
  justify-content: space-between;
}

.comment-user {
  font-weight: bold;
  font-size: 20px;
}
.comment-content {
  margin-left: 20px;
  font-size: 20px;
}
.commentcud{
  flex-direction: row;
  justify-content: flex-end;
}
.deleteC{
  margin-left:10px;
}
</style>