/*
Tạo một hàm kiểm tra email nhập vào xem có phải là email hay không
*/
function isEmail(inputEmail) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
	return regex.test(inputEmail);
}

function validatePassword(inputPassword) {
	return inputPassword.length > 4;
}

$(document).ready(function(){
    $('#username').change(function() {
        var username = $(this).val().trim();
            if(!isEmail(username)) {
            $("#alerts").html("Không đúng định dạng mail");
        } else {
            $("#alerts").html("");
        }
    });

    $('#passwd').change(function(){
        var passwd = $(this).val().trim();
            if(!validatePassword(passwd)) {
			$("#alerts").html("Mật khẩu phải tối thiểu 5 ký tự");
		} else {
			$("#alerts").html("");
		}
    });

});