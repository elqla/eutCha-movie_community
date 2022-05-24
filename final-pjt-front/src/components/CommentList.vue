<template>
  <div>
    <h3>{{ comment.id }}번 댓글 내용: {{ comment.content }}</h3>
    <p>댓글 쓴 사람 : {{ comment.user.username }} 닉네임 : {{ comment.user.nickname }}</p>
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

</style>