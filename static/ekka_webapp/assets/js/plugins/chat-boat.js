(function($) {
    "use strict";
/*--------------------- Start Chat Boat ---------------------- */
    //simple method to give random item from array
    var randomItem = function(array){return array[Math.floor(Math.random() * array.length)];};
    
    var username = "Stranger";
    
   var maxAttention123 = 45;

   var kid = {
    WPM: 80,//typing speed aka time it takes to type response
    status: "not connected",
    maxAttention: maxAttention123,//how long in seconds before kid gets bored and leaves
    curAttentionSpan: maxAttention123,//start at max
    curUsername: "Kid",
    usernames: [
        "John",
        "Marlee",
        "Anthony",
        "Bogata",
        "Brdina",
        "Burlin",
        "Helsinky",
        "Pardio",
        "Bhavlo",
    ],
    greetings: [
        "Hi",
        "Heya",
        "Hello!",
        "Hello Sir",
        "Hey Mam",
        "Hello you",
        "Hi there!",
    ],
    insults: [
        "How are you?",
        "ur product",
        "buddy",
        "u purchased???",
        "ur already purchased",
        "u want to purchase anything more?",
        "u having any problem ?",
        "like your kindness, sir",
        "Hope you will purchased again..",
        "please suggest to your friend",
        "do you like shirt & jeans quality ",
        "i bet you'd like beaty product..",
        "thats what i thought sir/mam",
        "are u a guy/girl? u sound pretty guy",
        "get 5product and having enjoyee this item",
        "i bet can't get anything missing on our site",
        "my service is to help you out for an issue",
        "guess who just got done and purchased other stuff",
        "think of that one all by yourself? aw how kind you are",
        "that's what i said to ur friends but please share it",
        "i bet it took u a long time to having a good product",
        "sorry, i was little busy with other customer",
        "i bet, you sound like you love taking it in the cart",
        "what was that? couldnt hear u well please try to explain your issue",
        "sorry i couldnt understand what u were saying cus ur english little slower",
    ],
    copypastas: [
        "( ͡° ͜ʖ ͡°)",
        "( ͡°╭͜ʖ╮͡° ) Helping to your valuable customer ( ͡°╭͜ʖ╮͡° )",
        "(◕‿◕✿) Kawaii in the saree. Purchase with huge Discount ( ͝° ͜ʖ͡°)",
        "Gr8 b8, m8. I rel8, str8 appreci8, and congratul8. I r8 this b8 an 8/8. Plz no h8, I'm str8 ir8.",
        "What the thing did you just say about our site, I’ll have you know I graduated top of my service, and I’ve been involved in your issue, and I will solve it out.",
        "💯💯At the End 😂😂😂 Sir 👌i AM 👉LITERALLY👈 iN 😂TEARS😂 RIGHT NOW 👆👇👉👈 hHAHAHAHAHAHAHA ✌️👌👍 TAHT You are FUNNY DUd 💧💧😅😂💦💧I cAN NOT Help you how 💯FUNny 👌👍💯thta shit wa s 👀👍😆😂😂😅 I 👦 CAN NOT ❌ bRATHE 👃👄👃👄❌❌ / HELP ❗️I NEEd 👉👉 AN a m b u l a n c e🚑🚑 SSSooOOoo00000oOOOOOøøøØØØØØ f**kING FUNY ✔️☑️💯💯1️⃣0️⃣0️⃣😆😆😂😂😅 shit man ❕💯💯🔥☝️👌damn",
    ],
    afkAlmostGone: [
        "...?",
        "lol scared sir?",
        "whats wrong, scared?",
        "whered you go sir/mam?",
        "having trouble thinking of a comeback to ping me?",
        "if you dont respond in 2 seconds that means you are 100% gone",
    ],
    afkGoodbyes: [
        "Wait this im out, Sir",
        "alright im out, Sir/Mam",
        "i gotta go now, cya Sir",
        "sorry gotta go get laid, cya Bye",
        "alright well im gonna go now, later will ping you",
        "alright guess ur not there anymore, cya Bye",
        "airght since ur being such a kind person, later on",
    ],
    triggers: [
        //something to keep in mind is that these are in order of importance
        [
            //so if two matches are triggered, the first one will be used
            new RegExp(".*(?:i (?:(?:got(?:ta| to))|have to) go|i'?m .*leav(?:e|ing)|bye+|cya|p(?:ea)?ce|gtg).*", 'gi'),
            [
                "bye Sir",
                "cya Sir",
                "cya Mam",
                "lol k cya...",
                "yea ok bye now",
                "yea go ahead and leave sir",
            ]
        ],
        [
            new RegExp(".*(?:(?:user)?name)[^?]*", 'gi'),
            [
                'at least my product is better than other site',
                'my product is an qaulity stands for i get all the customer',
                'at least my product is better than other, u will got good one',
            ]
        ],
        [
            new RegExp('.*(?:old|\d ?y\/?o|y(?:ea)?rs? old|age|young).*', 'gi'),
            [
                "im help you anytime..",
                "you will got full help from us",
                "actually im busy with other stuff..",
                "im actually busy with other customer",
            ]
        ],
        [
            new RegExp(".*(?:(?:yo)?u (?:are|r)|ur|you'?re)(?! not).*(?:retard|idiot|stupid|dumb).*", 'gi'),
            [
                "k...?",
                "look in a product",
                "hey news flash retard, look in a product",
                "u must be a kind while calling ME, look in a product",
                "wow sir ur, i bet ur friends is aiting to buy this product",
            ]
        ],
    ],
        reply: function(text){
            this.status = "typing";
            var kidName = this.curUsername;
            var kidWPM = this.WPM;
            var kidReply = "";
            var isCopyPasta = false;
            if(text !== undefined && text !== null && text !== ""){ 
                kidReply = text; 
            } else {				
                if($(".ec-chatbox .messages-wrapper .you").length === 1){
                kidReply = randomItem(this.greetings);
                }else{
                    var finalDecision = randomItem(this.insults);
                    var lastUserMessage = $(".ec-chatbox .message.you:last-child .text").text();
                    var triggered = false;
                    for(var i=0;i<this.triggers.length;i++){
                        var curRegex = this.triggers[i][0];
                        var randReply = randomItem(this.triggers[i][1]);
                        if(lastUserMessage.match(curRegex)){
                            console.log("TRIGGERED");
                            triggered = true;
                            finalDecision = randReply;
                            break;
                        }
                    }
                    if(Math.random() < 0.1 && !triggered){
                    finalDecision = randomItem(this.copypastas);
                    isCopyPasta = true;
                    }
                    kidReply = finalDecision;
                }
            }
            
            //function to simulate actual typing using WPM to estimate how long it'd take to type up a reply
            var sendReply = function(replyText, isPasta){
                setTimeout(function(){
                sendMsg(kidName, replyText);
                kid.status = "idle";
                $(".typing-msg").remove();
                console.log("done typing! took "+(replyText.length * (1000/((kidWPM * 6)/60)))+"ms to reply");
                }, isPasta?500:(replyText.length * (1000/((kidWPM * 6)/60))));
            };
            //function to delay response time (so kid doesnt start typing response instantly)
            setTimeout(function(){
                
                var html = '<div class="them message typing-msg">'+
                        '<div class="avatar">'+
                            '<img class="chat-user-img" src="assets/images/chatboat/helper.png"/>'+
                        '</div>'+
                        '<div class="name">'+
                            '<svg style="margin: auto;display: block;shape-rendering: auto;width: 43px;height: 20px;" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid"><circle cx="0" cy="44.1678" r="15" fill="#888ea8"><animate attributeName="cy" calcMode="spline" keySplines="0 0.5 0.5 1;0.5 0 1 0.5;0.5 0.5 0.5 0.5" repeatCount="indefinite" values="57.5;42.5;57.5;57.5" keyTimes="0;0.3;0.6;1" dur="1s" begin="-0.6s"></animate></circle> <circle cx="45" cy="43.0965" r="15" fill="#888ea8"><animate attributeName="cy" calcMode="spline" keySplines="0 0.5 0.5 1;0.5 0 1 0.5;0.5 0.5 0.5 0.5" repeatCount="indefinite" values="57.5;42.5;57.5;57.5" keyTimes="0;0.3;0.6;1" dur="1s" begin="-0.39999999999999997s"></animate></circle> <circle cx="90" cy="52.0442" r="15" fill="#888ea8"><animate attributeName="cy" calcMode="spline" keySplines="0 0.5 0.5 1;0.5 0 1 0.5;0.5 0.5 0.5 0.5" repeatCount="indefinite" values="57.5;42.5;57.5;57.5" keyTimes="0;0.3;0.6;1" dur="1s" begin="-0.19999999999999998s"></animate></circle></svg>'+
                        '</div>'+
                    '</div>';
                        
                $(".ec-chatbox .messages-wrapper").append($.parseHTML(html));
                $(".ec-chatbox").scrollTop($(".ec-chatbox .messages-wrapper").height());
                    
                sendReply(kidReply, isCopyPasta);
            },(250+(Math.random()*5000)));
        },
    };
    
    //start attention span countdown
    var timerActive = false, almostAFK = false;
    var attentionTimer = function(){
        var timer = setInterval(function(){
            //console.log(kid.curAttentionSpan+" "+almostAFK);
            if(kid.curAttentionSpan > 0){
                if(kid.status === "idle"){
                    kid.curAttentionSpan--;
                }
                if(!almostAFK && kid.curAttentionSpan <= kid.maxAttention - (kid.maxAttention / 2)){
                    almostAFK = true;
                    if(kid.status !== "typing"){kid.reply(randomItem(kid.afkAlmostGone));}
                }
            } else {
                if(kid.status !== "typing"){
                    kid.reply(randomItem(kid.afkGoodbyes));
                    kid.status = "disconnected";
                    clearInterval(timer);
                }
            }
        }, 1000);
    };
    
    //function to add message to window, if who === username, it's your message, otherwise its the stranger
    var sendMsg = function(who, text){
        if(text === null || text === undefined || text === ""){return;}
        
        if($(".ec-reply input.usermsg").attr("placeholder") != ""){
            $(".ec-reply input.usermsg").attr("placeholder","");
        }

        var curntTime = formatAMPM(new Date);
        
        var html = '<div class="'+(who === username?"you":"them")+' message">'+
                        '<div class="avatar">'+
                            '<img class="chat-user-img" src="assets/images/chatboat/'+(who === username?"customer":"helper")+'.png"/>'+
                        '</div>'+
                        '<div class="name">'+
                            '<p class="user-name">'+who+'</p>'+
                            '<p class="user-text">'+text+'</p>'+
                            '<span class="msg-time">'+curntTime+'</span>'+
                        '</div>'+
                    '</div>';

        $(".ec-chatbox .messages-wrapper").append($.parseHTML(html));
        $(".ec-chatbox").scrollTop($(".ec-chatbox .messages-wrapper").height());
        
        if(who === username){
            if(!timerActive){
                timerActive = true;attentionTimer();
            }
            kid.curAttentionSpan = kid.maxAttention;
            almostAFK = false;
            if(kid.status !== "typing"){
                kid.reply();
            }
            $(".ec-reply input.usermsg").val("");
        }
    };
    
    //function to set initial username
    $(".ec-setuser button").click(function(){
        var desiredName = $(".ec-setuser .username").val();
        var userEmail = $(".ec-setuser .useremail").val();
        var userReson = $(".ec-setuser .userreson").val();

        if(desiredName !== "" && desiredName !== null && desiredName !== undefined){
            username = desiredName;
            $(".ec-setuser, .ec-dim").fadeOut(100);
            setTimeout(function(){
                
                var dateMonthYear = getDateMonthYear();
                $(".messages-wrapper .status").text(dateMonthYear);
                $(".ec-reply input.usermsg").prop('disabled', false);
                kid.status = "idle";
                kid.curUsername = randomItem(kid.usernames);
            },(500+(Math.random()*1000)));
        } else {
            alert("Please enter a username.");
            $(".ec-setuser input.username").focus();
        }
    });
    
    //send user's typed message when send button or enter key is pressed
    $(".ec-reply input.usermsg").keydown(function(e){
        if(e.which === 13){
            sendMsg(username, $(this).val());
        }
    });
    
    $(".ec-reply button.send").click(function(){
        sendMsg(username, $(".ec-reply input.usermsg").val());$(".ec-reply input.usermsg").focus();
    });

    function formatAMPM(date) {
        var hours = date.getHours();
        var minutes = date.getMinutes();
        var ampm = hours >= 12 ? 'pm' : 'am';
        hours = hours % 12;
        hours = hours ? hours : 12; // the hour '0' should be '12'
        minutes = minutes < 10 ? '0'+minutes : minutes;
        var strTime = hours + ':' + minutes + ' ' + ampm;
        return strTime;
    }
    // console.log(formatAMPM(new Date));

    function getDateMonthYear(){
        var today = new Date();
        var date = today.getDate();
        var month = today.getMonth();
        var year = today.getFullYear();
        var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        return dateMonthYear = date+', '+months[month]+' '+year;
    }					
    
    var dateMonthYear = getDateMonthYear();
    $(".messages-wrapper .status").text(dateMonthYear);

    $('.ec-float-chat').on('click', function(){
        
        var isClass = $('.ec-chat').hasClass('animate__fadeInRight');
        if(isClass){
            $('.ec-chat').removeClass('animate__fadeInRight');	
            $('.ec-chat').addClass('animate__fadeOutRight');	
        } else {
            $('.ec-chat').removeClass('animate__fadeOutRight');	
            $('.ec-chat').addClass('animate__fadeInRight');
        }	
    });		
            
/*--------------------- End Chat Boat ---------------------- */
})(jQuery);