*Being Polite*

Mama taught me to be polite when folks mis-dialed our phone number.
Well, by my way of thinking, the principle should apply to them internets as well. 
Judging by the logs of some websites I maintain, 
there are quite a few folks who have trouble getting their urls correct.

Some of them fellas must have some urgent business. 
Why else would they being trying to contact pages like "admin/config.php"?
So ponder the situation from that fellas point of view.
How frustrating it must be to simply get a rude "page not found" message!

Whilst doing some of my whittlin' I comes up with what I reckon is a pretty good notion.
Good enough, me thinks, to share with y'all.
How much more soothing and pleasant would it be to be redirected to some nice music?
And what could be more soothing than a video of Rick Astley playing
*Never Gonna Give You Up*?

So here is my simple Python code, written for Flask, that y'all can mimic if you want to be polite like me.
It is written in Python, 'cause I am fond of snakes.
(And don't be telling Mama about my fondness for a Flask or two of the good stuff.)

Mostly Important Notes:
 * You really only need "hacker_urls.py" and "rickroll.py". The other files are just me showing off.
 * You can set a logger method with *set_rickroll_logger(my_logger_method)*. That can help keep track of, as Papa would say, "What in tarnation is going on here?".
 * You can change the redirect url using an environment variable of RICKROLL_URL. That might be good cover if your legal department starts to suspect you are channeling your inner Dennis Nedry.
 * Blueprints are pretty darn handy, but don't get too fancy and add a prefix, or the whole point is spoiled. Poor fella in a hurry ain't likely to type "prefix/admin/config.php" when he is used to the shorter version.
 * Some of the fellas we are trying to be all polite with must have trouble remembering website names because they use IP addresses. So they use "http://128.0.5.6/" instead of "http://example.com/". You can show them some politeness by noticing the absence of your domain name on your root "/" page and then doing a *return rickroll()*.
 * The code uses a black list harvested from logs. Feel free to contribute additions with a PR.
 * Simply white listing your own good urls is probably a bad technique. Your more upright and classy users could easily fat finger an incorrect url themselves.  Or you could decide to readjust your routing and which then messes up with someone's browser bookmark.
 * Do glance through the list of hacker urls in case one or more are legitimate urls on your site.
 * If Rick Astley had had teachers like I had he would have fixed the grammar and called his song *Never Going To Be Giving You Up*. That also sounds a little less stalker-ish.