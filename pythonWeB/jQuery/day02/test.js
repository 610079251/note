//页面加载后就执行
$(function(){
	//为 #btn 绑定事件
	$("#btn").click(function(){
		$("#show").html($("#info").val());
	});
});