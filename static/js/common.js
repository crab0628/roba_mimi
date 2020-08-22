// 自分以外もわかるよう、コメントはしつこいくらい入れましょう！
// js効いてるか確認用
// $(function(){
//     'use strict';

//     alert('アラートだよ〜。');

// })();

$(function () {

  // アイコン選択
  $(function () {
    $('.icons').click(function () {
      $('.active_icon').removeClass('active_icon');

      // 変数clickedIndexを定義し、クリックしたボタンのインデックス番号を代入してください
      var clickedIndex = $('.icons').index($(this));

      // eqの引数をclickedIndexに書き換えてください
      $('.selected_icon').eq(clickedIndex).addClass('active_icon');

      // テキストエリアの中身書き換え
      var textValue = $('.selected_icon').eq(clickedIndex).val();
      console.log(textValue);
      $('textarea').attr('placeholder', textValue);
    });
  });



  // text img ボタン切り替え
  $(function () {
    $('.switch_btn').click(function () {
      $('.active').removeClass('active');

      // 変数clickedIndexを定義し、クリックしたボタンのインデックス番号を代入してください
      var clickedIndex = $('.switch_btn').index($(this));

      // eqの引数をclickedIndexに書き換えてください
      $('.form').eq(clickedIndex).addClass('active');
    });
  });


  // 試し①
  // $(function() {
  //   $('#file-sample').on('change', function(e) {
  //       // 1枚だけ表示する
  //       var file = e.target.files[0];

  //       // ファイルのブラウザ上でのURLを取得する
  //       var blobUrl = window.URL.createObjectURL(file);

  //       // img要素に表示
  //       $('#file-preview').attr('src', blobUrl);
  //   });
  // });  

  // 試し②
  $(function () {
    $('p[class=fl]').after('<span></span>');

    // アップロードするファイルを選択
    $('input[type=file]').change(function () {
      var file = $(this).prop('files')[0];

      // 画像以外は処理を停止
      if (!file.type.match('image.*')) {
        // クリア
        $(this).val('');
        $('span').html('');
        return;
      }

      // 新幅・高さ
      var new_w = 120;
      var new_h = 120;

      // 画像表示
      var reader = new FileReader();
      reader.onload = function () {
        var img_src = $('<img>').attr('src', reader.result);

        var org_img = new Image();
        org_img.src = reader.result;
        org_img.onload = function () {
          // 元幅・高さ
          var org_w = this.width;
          var org_h = this.height;
          // 幅 ＜ 規定幅 && 高さ ＜ 規定高さ
          if (org_w < new_w && org_h < new_h) {
            // 幅・高さは変更しない
            new_w = org_w;
            new_h = org_h;
          } else {
            // 幅 ＞ 規定幅 || 高さ ＞ 規定高さ
            if (org_w > org_h) {
              // 幅 ＞ 高さ
              var percent_w = new_w / org_w;
              // 幅を規定幅、高さを計算
              new_h = Math.ceil(org_h * percent_w);
            } else if (org_w < org_h) {
              // 幅 ＜高さ
              var percent_h = new_h / org_h;
              // 高さを規定幅、幅を計算
              new_w = Math.ceil(org_w * percent_h);
            }
          }

          // リサイズ画像
          $('span').html($('<canvas>').attr({
            'id': 'canvas',
            'width': new_w,
            'height': new_h
          }));
          var ctx = $('#canvas')[0].getContext('2d');
          var resize_img = new Image();
          resize_img.src = reader.result;
          ctx.drawImage(resize_img, 0, 0, new_w, new_h);
        };
      }
      reader.readAsDataURL(file);
    });
  });
});