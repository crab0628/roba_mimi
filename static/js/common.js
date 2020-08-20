// 自分以外もわかるよう、コメントはしつこいくらい入れましょう！
// js効いてるか確認用
// $(function(){
//     'use strict';

//     alert('アラートだよ〜。');

// })();

// text img ボタン切り替え
$(function() {
    $('.switch_btn').click(function() {
      $('.active').removeClass('active');
      
      // 変数clickedIndexを定義し、クリックしたボタンのインデックス番号を代入してください
      var clickedIndex = $('.switch_btn').index($(this));
      
      // eqの引数をclickedIndexに書き換えてください
      $('.form').eq(clickedIndex).addClass('active');
    });
  });
  
  