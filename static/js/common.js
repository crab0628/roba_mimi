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
  

// ①試し
$(function() {
  $('#file-sample').on('change', function(e) {
      // 1枚だけ表示する
      var file = e.target.files[0];

      // ファイルのブラウザ上でのURLを取得する
      var blobUrl = window.URL.createObjectURL(file);

      // img要素に表示
      $('#file-preview').attr('src', blobUrl);
  });
});  

