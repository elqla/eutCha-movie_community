<template>
  <div class="d-flex comment-item">
    <div class="comment-user">{{ comment.user.username }}, 닉네임 : {{ comment.user.nickname }}</div>
    <div class="comment-content">{{ comment.content }}</div>
  </div>
</template>

<script>
export default {
  name: 'CommentList',
  props: {
    comment: Object,
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
}

.comment-user {
  font-weight: bold;
  font-size: 20px;
}
.comment-content {
  margin-left: 20px;
  font-size: 20px;
}
</style>