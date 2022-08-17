// var today = new Date();
const year = new Date().getFullYear();
const month = new Date().getMonth();
const date = new Date().getDate();
const fourthOfJuly = new Date(year, month, date + 2).getTime();



// get today's date
const today = new Date().getTime();

// get the difference
let diff;
diff = fourthOfJuly - today;
	
// math
let days = Math.floor(diff / (1000 * 60 * 60 * 24));
let hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
let minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
let seconds = Math.floor((diff % (1000 * 60)) / 1000);

// display
document.getElementById("timer").innerHTML =
'<div class="days"> \
<div class="numbers">' +
days +
'</div>days</div> \
<div class="hours"> \
<div class="numbers">' +
hours +
'</div>hours</div> \
<div class="minutes"> \
<div class="numbers">' +
minutes +
'</div>minutes</div> \
<div class="seconds"> \
<div class="numbers">' +
seconds +
"</div>seconds</div> \
</div>";

// countdown
let timer = setInterval(function () {
	
	const today = new Date().getTime();
	
	let diff;
	diff = fourthOfJuly - today;
	
	let days = Math.floor(diff / (1000 * 60 * 60 * 24));
	let hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
	let minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
	let seconds = Math.floor((diff % (1000 * 60)) / 1000);
	
	document.getElementById("timer").innerHTML =
    '<div class="days"> \
	<div class="numbers">' +
    days +
    '</div>days</div> \
	<div class="hours"> \
	<div class="numbers">' +
    hours +
    '</div>hours</div> \
	<div class="minutes"> \
	<div class="numbers">' +
    minutes +
    '</div>minutes</div> \
	<div class="seconds"> \
	<div class="numbers">' +
    seconds +
    "</div>seconds</div> \
	</div>";
}, 1000);
