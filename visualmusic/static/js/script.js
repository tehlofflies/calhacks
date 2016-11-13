// take txt file of sentiments and change color scheme colors
// adjust colors according to sentiment
// rgb values (0, 0, 0)
// anger is red, allow colors to transition from (R *(1-sentiment), G, B) to (R *(1+sentiment), G, B)
// joy is yellow, so adjust green and red; fear is purple so adjust red and blue; 
// sadness is blue; disgust is brown/black, so adjust red, green, and blue

// css adjustments in javascript
// give elements properties "transition: all 1s ease"


// theme 0:
// svg circle, svg rect {
//  fill: #F7D11E; (247,209,30)
//  stroke: #F27F40; (242,127,64)

// path {
//   fill: #f88e22; (248,142,34)
// }

$(function () {
	$.get('sentiments.txt', function(data) {
	   console.log(data)
	}, 'text');
})