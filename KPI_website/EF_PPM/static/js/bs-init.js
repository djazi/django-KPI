$(document).ready(function(){

	$('[data-bs-chart]').each(function(index, elem) {
		this.chart = new Chart($(elem), $(elem).data('bs-chart'));
	});

});

	function getSelectValue() {
            var selectedValue = document.getElementById("list").value;
            alert(selectedValue);
        }
        getSelectValue();
 