/*! jQuery Instagram - v0.3.1 - 2014-06-19
* http://potomak.github.com/jquery-instagram
* Copyright (c) 2014 Giovanni Cappellotto; Licensed MIT */
!function(a){function b(b){var c="https://api.instagram.com/v1",d={};if(null==b.accessToken&&null==b.clientId)throw"You must provide an access token or a client id";if(d=a.extend(d,{access_token:b.accessToken||"",client_id:b.clientId||"",count:b.count||""}),null!=b.url)c=b.url;else if(null!=b.hash)c+="/tags/"+b.hash+"/media/recent";else if(null!=b.search)c+="/media/search",d=a.extend(d,b.search);else if(null!=b.userId){if(null==b.accessToken)throw"You must provide an access token";c+="/users/"+b.userId+"/media/recent"}else null!=b.location?(c+="/locations/"+b.location.id+"/media/recent",delete b.location.id,d=a.extend(d,b.location)):c+="/media/popular";return{url:c,data:d}}a.fn.instagram=function(c){var d=this;c=a.extend({},a.fn.instagram.defaults,c);var e=b(c);return a.ajax({dataType:"jsonp",url:e.url,data:e.data,success:function(a){d.trigger("didLoadInstagram",a)}}),this.trigger("willLoadInstagram",c),this},a.fn.instagram.defaults={accessToken:null,clientId:null,count:null,url:null,hash:null,userId:null,location:null,search:null}}(jQuery);