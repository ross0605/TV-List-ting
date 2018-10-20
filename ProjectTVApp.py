from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def wrong():
	return redirect(url_for('root'))

@app.errorhandler(404)
def page_not_found(error):
	return "Oops, I couldn't find the page you requested. Try going to http://set09103.napier.ac.uk:9147/home to return to the homepage", 404



@app.route('/home')
def root():
	return render_template('homeInherit.html'), 200

@app.route('/categories/a-z-list')
def azlist():
	return render_template('azInherit.html'), 200

@app.route('/categories/ratings')
def ratingslist():
        return render_template('ratingsInherit.html'), 200

@app.route('/categories/genres')
def genreslist():
        return render_template('genresInherit.html'), 200

@app.route('/categories/a-z-list/24-hours-in-a&e')
@app.route('/categories/ratings/24-hours-in-a&e')
@app.route('/categories/genres/documentary/24-hours-in-a&e')
def programme24():
	bg='#2b4775'
	Title='24 Hours in A&E'
	Programme='24 Hours in A&E'
	Channel='Channel 4, Wednesday 9pm'
	ImgSrc='/static/24H.jpg'
	ImagePage='http://set09103.napier.ac.uk:9147/24-hours-in-a&e/24H.jpg'
	Rating='8/10 IMDb Rating'
	Section1="""24 Hours in A&E is a British documentary programme, set in a teaching hospital in inner London. Cameras film round the clock for 28 days, 24 hours a day in A&E. The Channel 4 documentary series gives viewers behind the scenes access to the Accident & Emergency Department. 
Series one aired every Wednesday at 21:00 and consisted of 14 one-hour episodes. The filming took place over 28 days using 70 fixed cameras and is the largest documentary series Channel 4 has ever made.
The series enables viewers to see the unique set of challenges - including the highs and lows - that A&E staff face as they treat the hundreds of patients that come through the doors every day.
The episodes show how the staff work as a team to treat those patients present involved in a full range of minor and serious conditions, both medical (suspected heart attack, aortic abdominal aneurysm, stroke) and trauma (from household accidents to road traffic collisions). The fly-on-the-wall footage is intercut with subsequent interviews with staff, patients and relatives giving their perspectives and background on the events shown.
As of 1 May 2017, there have been 12 series and 155 episodes (+2 specials)."""
	IMDBLink='IMDb page'
	Link='https:www.imdb.com/title/tt0096555'
	return render_template('pageBase.html', BackgroundColour=bg, ImagePage=ImagePage, Title=Title, Programme=Programme, Channel=Channel, ImgSrc=ImgSrc, Rating=Rating, Section1=Section1, IMDBLink=IMDBLink, Link=Link), 200




@app.route('/categories/a-z-list/the-apprentice')
@app.route('/categories/ratings/the-apprentice')
@app.route('/categories/genres/reality/the-apprentice')
def programmeapprentice():
	bg='#1a2e4f'
        Title='The Apprentice'
        Programme='The Apprentice'
        Channel='BBC One, Wednesday 9pm'
        ImgSrc='/static/Apprentice.jpg'
	ImagePage='http://set09103.napier.ac.uk:9147/the-apprentice/Apprentice.jpg'
        Rating='7.3/10 IMDb Rating'
        Section1="""The Apprentice is a British business-styled reality game show, created by Mark Burnett, distributed by Fremantle and broadcast by the BBC. 
Based upon the American original of the same name and billed as the "job interview from hell", the programme focuses on a group of aspiring businesspeople competing against each other in a series of business related challenges, in order to win a prize offered by British business magnate Lord (Alan) Sugar. Produced by a number of companies over the course of the show\'s history, including Talkback Thames and United Artists Media Group, each series consists of around twelve episodes, and were initially aired either around early/late Spring, before later series began their broadcasts around Autumn. The show initially was aired on BBC Two, before the programme\'s success led the BBC to move the show to BBC One from the start of the third series in 2007. 
Since its second series, the show is accompanied by a companion discussion show entitled The Apprentice: You\'re Fired! that runs alongside a series\' broadcast. In addition, the programme has also spawned two celebrity versions for Comic Relief and Sport Relief, and a number of special 60-minute episodes, concentrating on the candidates that were fired in the current series being broadcast or those who made it to its penultimate/final stage. While the programme has been compared to another BBC series, Dragons\' Den, its success has led to the creation of Apprentice-related merchandising including a magazine, podcast, and official books, while leading other production companies to produces shows that follow a similar format, including Tycoon, Beat the Boss, and Election.
At present, the show has run for thirteen series and a total of 156 episodes. On 20 September 2018, it was revealed by Lord Sugar that the show\'s fourteenth series had been filmed and set for broadcast on 3 October."""
        IMDBLink='IMDb page'
        Link='https:www.imdb.com/title/tt0450897'
        return render_template('pageBase.html', BackgroundColour=bg, Title=Title, Programme=Programme, Channel=Channel, ImgSrc=ImgSrc, Rating=Rating, Section1=Section1, IMDBLink=IMDBLink, Link=Link, ImagePage=ImagePage), 200





@app.route('/categories/a-z-list/bbc-news')
@app.route('/categories/ratings/bbc-news')
@app.route('/categories/genres/news/bbc-news')
def programmebbc():
	bg='#9e1919'
        Title='BBC News'
        Programme='BBC News'
        Channel='BBC One, Every day 9am, 1pm, 6pm, 10pm'
        ImgSrc='/static/BBC.jpg'
	ImagePage='http://set09103.napier.ac.uk:9147/bbc-news/bbc.jpg'
        Rating='7.3/10 IMDb Rating'
        Section1="""BBC News is an operational business division of the British Broadcasting Corporation (BBC) responsible for the gathering and broadcasting of news and current affairs. The department is the world's largest broadcast news organisation and generates about 120 hours of radio and television output each day, as well as online news coverage. The service maintains 50 foreign news bureaus with more than 250 correspondents around the world. James Harding has been Director of News and Current Affairs since April 2013.
The department's annual budget is in excess of 350 million; it has 3,500 staff, 2,000 of whom are journalists. BBC News' domestic, global and online news divisions are housed within the largest live newsroom in Europe, in Broadcasting House in central London. Parliamentary coverage is produced and broadcast from studios in Millbank in London. Through the BBC English Regions, the BBC also has regional centres across England, as well as national news centres in Northern Ireland, Scotland and Wales. All nations and English regions produce their own local news programmes and other current affairs and sport programmes.
The BBC is a quasi-autonomous corporation authorised by Royal Charter, making it operationally independent of the government, who have no power to appoint or dismiss its director-general, and required to report impartially. As with all major media outlets, though, it has been accused of political bias from across the political spectrum, both within the UK and abroad.
"""
        IMDBLink='IMDb page'
        Link='https:www.imdb.com/title/tt0344621'
        return render_template('pageBase.html', BackgroundColour=bg, Title=Title, Programme=Programme, Channel=Channel, ImgSrc=ImgSrc, Rating=Rating, Section1=Section1, IMDBLink=IMDBLink, Link=Link, ImagePage=ImagePage), 200




@app.route('/categories/a-z-list/big-brother')
@app.route('/categories/ratings/big-brother')
@app.route('/categories/genres/reality/big-brother')
def programmebb():
	bg='#293e84'
        Title='Big Brother'
        Programme='Big Brother'
        Channel='Channel 5, Monday-Friday 9pm, Sunday 9pm'
        ImgSrc='/static/BigBro.jpg'
	ImagePage='http://set09103.napier.ac.uk:9147/big-brother/BigBro.jpg'
        Rating='4.3/10 IMDb Rating'
        Section1="""Big Brother is the British version of the international reality television franchise Big Brother created by producer John de Mol in 1997. The show follows a number of contestants, known as housemates, who are isolated from the outside world for an extended period of time in a custom built house. Each week, one of the housemates is evicted by a public vote, with the last housemate remaining winning a cash prize. The series takes its name from the character in George Orwell's 1949 novel Nineteen Eighty-Four. The series premiered on 18 July 2000 on Channel 4, and immediately became a ratings hit. The series also featured a 24-hour live feed, in which fans could view inside the house at any time. Big Brother aired for eleven series on Channel 4, followed by one final special edition, Ultimate Big Brother, which ended on 10 September 2010. Following this, Channel 5 acquired the rights to the series, and it was officially relaunched on 18 August 2011. In 2014, Emma Willis announced that the show would be back for a sixteenth series in 2015. It was announced on 19 March 2015 that the show would remain on air until at least 2018. 
The show was initially presented by Davina McCall from its inception to its cancellation by Channel 4. Despite being offered the position of presenter following the show's move to Channel 5, McCall chose not to return. Former winner Brian Dowling became the presenter, a position he held throughout the twelfth and thirteenth series. Emma Willis later replaced Dowling as the presenter of the series from the fourteenth series onwards. Marcus Bentley has been the narrator of the series since it premiered in 2000. Big Brother has had numerous spin-off series occur since its premiere, most notably Celebrity Big Brother, which is a shorter version of the main series wherein the cast is composed solely of celebrities. Numerous other spin-off series that are not competition based have aired, with Dermot O'Leary, Russell Brand, George Lamb, and Emma Willis all presentering spin-offs. Over the course of its run, there will have been a total of 45 series of Big Brother in the UK: nineteen regular series, twenty two celebrity series and four other series. Currently, it is the third longest running version of Big Brother to date, following the Spanish and American adaptations.
On 14 September 2018, Channel 5 announced that Big Brother and Celebrity Big Brother would not be returning to the channel after the end of the'Casualty, stylised as CASUAL+Y, is a British medical drama series that airs weekly on BBC One (sometimes with a short break in the summer between series, but not always). It is the longest-running emergency medical drama television series in the world, and the most enduring medical drama shown on prime time television in the world. Created by Jeremy Brock and Paul Unwin, it was first broadcast in the United Kingdom on BBC One on 6 September 1986. The original producer was Geraint Morris.'
 nineteenth regular series which will end on 5 November 2018."""
        IMDBLink='IMDb page'
        Link='https:www.imdb.com/title/tt0257295'
        return render_template('pageBase.html', BackgroundColour=bg, Title=Title, Programme=Programme, Channel=Channel, ImgSrc=ImgSrc, Rating=Rating, Section1=Section1, IMDBLink=IMDBLink, Link=Link, ImagePage=ImagePage), 200





@app.route('/categories/a-z-list/breaking-bad')
@app.route('/categories/ratings/breaking-bad')
@app.route('/categories/genres/drama/breaking-bad')
def programmebreakingbad():
	bg='#0a5438'
        Title='Breaking Bad'
        Programme='Breaking Bad'
        Channel='HBO'
        ImgSrc='/static/Breaking.jpg'
	ImagePage='http://set09103.napier.ac.uk:9147/breaking-bad/Breaking.jpg'
        Rating='9.5/10 IMDb Rating'
        Section1="""Breaking Bad is an American neo-western crime drama television series created and produced by Vince Gilligan. The show originally aired on the AMC network for five seasons, from January 20, 2008 to September 29, 2013. Set and filmed in Albuquerque, New Mexico, the series tells the story of Walter White (Bryan Cranston), a struggling and depressed high school chemistry teacher who is diagnosed with lung cancer. Together with his former student Jesse Pinkman (Aaron Paul), White turns to a life of crime by producing and selling crystallized methamphetamine to secure his family's financial future before he dies, while navigating the dangers of the criminal world. The title comes from the Southern colloquialism \"breaking bad\", meaning to \"raise hell\" or turn to a life of crime.
Walter's family consists of his wife Skyler, son Walter, Jr., and daughter Holly. The show also features Skyler's sister Marie Schrader, her husband Hank, a DEA agent. Walter hires lawyer Saul Goodman, who connects him with private investigator and fixer Mike Ehrmantraut and in turn Mike's employer, drug kingpin Gus Fring. The final season introduces the characters Todd Alquist and Lydia Rodarte-Quayle.
Breaking Bad is widely regarded as one of the greatest television series of all time. By the time the series finale aired, it was among the most-watched cable shows on American television. The show received numerous awards, including 16 Primetime Emmy Awards, eight Satellite Awards, two Golden Globe Awards, two Peabody Awards, two Critics' Choice Awards and four Television Critics Association Awards. For his leading performance, Cranston won the Primetime Emmy Award for Outstanding Lead Actor in a Drama Series four times, while Aaron Paul won the Primetime Emmy Award for Outstanding Supporting Actor in a Drama Series three times; Anna Gunn won the Primetime Emmy Award for Outstanding Supporting Actress in a Drama Series twice. In 2013, Breaking Bad entered the Guinness World Records as the most critically acclaimed show of all time."""
        IMDBLink='IMDb page'
        Link='https:www.imdb.com/title/tt0903747'
        return render_template('pageBase.html', BackgroundColour=bg, Title=Title, Programme=Programme, Channel=Channel, ImgSrc=ImgSrc, Rating=Rating, Section1=Section1, IMDBLink=IMDBLink, Link=Link, ImagePage=ImagePage), 200






@app.route('/categories/a-z-list/casualty')
@app.route('/categories/ratings/casualty')
@app.route('/categories/genres/drama/casualty')
def programmecasualty():
	bg='#141616'
        Title='Casualty'
        Programme='Casualty'
        Channel='BBC One, Monday 9pm'
        ImgSrc='/static/Casualty.jpg'
	ImagePage='http://set09103.napier.ac.uk:9147/casualty/Casualty.jpg'
        Rating='6.1/10 IMDb Rating'
        Section1="""Casualty, stylised as CASUAL+Y, is a British medical drama series that airs weekly on BBC One (sometimes with a short break in the summer between series, but not always). It is the longest-running emergency medical drama television series in the world, and the most enduring medical drama shown on prime time television in the world. Created by Jeremy Brock and Paul Unwin, it was first broadcast in the United Kingdom on BBC One on 6 September 1986. The original producer was Geraint Morris. 
The programme is set in the fictional Holby City Hospital and focuses on the staff and patients of the hospital's Accident and Emergency Department. The show has very few ties to its sister programme Holby City, which began as a spin-off from Casualty in 1999, set in the same hospital. Casualty is shown weekly on a Saturday evening, which has been its time slot since the early 1990s.
Casualty's exterior shots were mainly filmed outside the Ashley Down Centre in Bristol from 1986 until 2002 when they moved to the centre of Bristol for just over nine years. In 2011, Casualty celebrated its 25th anniversary; following that, for the Bristol finale, they filmed the Emergency department catching fire and subsequently exploding. After 25 years in Bristol, Casualty moved to its new home at the Roath Lock Studios in Cardiff where it is currently filmed.
The 1,000th episode of Casualty aired on 25 June 2016. A feature-length 30th anniversary episode of Casualty aired on 27 August 2016, episode 1 of series 31. For the series 31 finale, creator Paul Unwin returned to write a special episode which was entirely recorded in one take using only one camera, five boom operators and forty microphones."""
        IMDBLink='IMDb page'
        Link='https:www.imdb.com/title/tt0096555'
        return render_template('pageBase.html', BackgroundColour=bg, Title=Title, Programme=Programme, Channel=Channel, ImgSrc=ImgSrc, Rating=Rating, Section1=Section1, IMDBLink=IMDBLink, Link=Link, ImagePage=ImagePage), 200



@app.route('/categories/a-z-list/friends')
@app.route('/categories/ratings/friends')
@app.route('/categories/genres/sitcom/friends')
def programmefriends():
	bg='#000000'
        Title='Friends'
        Programme='Friends'
        Channel='Comedy Central, Every day 7pm, 7:30pm, 8pm, 8:30pm'
        ImgSrc='/static/friends.jpg'
	ImagePage='http://set09103.napier.ac.uk:9147/friends/friends.jpg'
        Rating='8.9/10 IMDb Rating'
        Section1="""Friends is an American television sitcom, created by David Crane and Marta Kauffman, which aired on NBC from September 22, 1994 to May 6, 2004, lasting ten seasons. With an ensemble cast starring Jennifer Aniston, Courteney Cox, Lisa Kudrow, Matt LeBlanc, Matthew Perry and David Schwimmer, the show revolves around six 20 to 30 year old friends living in Manhattan, New York City. The series was produced by Bright/Kauffman/Crane Productions, in association with Warner Bros. Television. The original executive producers were Kevin S. Bright, Marta Kauffman, and David Crane.
Kauffman and Crane began developing Friends under the title Insomnia Cafe between November and December 1993. They presented the idea to Bright, and together they pitched a seven-page treatment of the show to NBC. After several script rewrites and changes, including a title change to Six of One, and, Friends Like Us, the series was finally named Friends. 
Filming of the show took place at Warner Bros. Studios in Burbank, California. All ten seasons of Friends ranked within the top ten of the final television season ratings; ultimately reaching the number one spot in its eighth season. The series finale, aired on May 6, 2004, was watched by around 52.5 million American viewers, making it the fifth most-watched series finale in television history, and the most-watched television episode of the 2000s decade. 
Friends received acclaim throughout its run, becoming one of the most popular television shows of all time. The series was nominated for 62 Primetime Emmy Awards, winning the Outstanding Comedy Series award in 2002 for its eighth season. The show ranked no. 21 on TV Guide's 50 Greatest TV Shows of All Time, and no. 7 on Empire magazine's The 50 Greatest TV Shows of All Time. In 1997, the episode "The One with the Prom Video" was ranked no. 100 on TV Guide's 100 Greatest Episodes of All-Time. In 2013, Friends ranked no. 24 on the Writers Guild of America's 101 Best Written TV Series of All Time, and no. 28 on TV Guide's 60 Best TV Series of All Time."""      
	IMDBLink='IMDb page'
        Link='https:www.imdb.com/title/tt0109778'
        return render_template('pageBase.html', BackgroundColour=bg, Title=Title, Programme=Programme, Channel=Channel, ImgSrc=ImgSrc, Rating=Rating, Section1=Section1, IMDBLink=IMDBLink, Link=Link, ImagePage=ImagePage), 200






@app.route('/categories/a-z-list/game-of-thrones')
@app.route('/categories/ratings/game-of-thrones')
@app.route('/categories/genres/fantasy/game-of-thrones')
def programmegot():
	bg='#334049'
        Title='Game of Thrones'
        Programme='Game of Thrones'
        Channel='HBO'
        ImgSrc='/static/Got.jpg'
	ImagePage='http://set09103.napier.ac.uk:9147/game-of-thrones/Got.jpg'
        Rating='9.5/10 IMDb Rating'
        Section1="""Game of Thrones is an American fantasy drama television series created by David Benioff and D. B. Weiss. It is an adaptation of A Song of Ice and Fire, George R. R. Martin's series of fantasy novels, the first of which is A Game of Thrones. It is filmed in Belfast and elsewhere in Northern Ireland, Canada, Croatia, Iceland, Malta, Morocco, Scotland, Spain, and the United States. The series premiered on HBO in the United States on April 17, 2011, and its seventh season ended on August 27, 2017. The series will conclude with its eighth season premiering in 2019. 
Set on the fictional continents of Westeros and Essos, Game of Thrones has several plot lines and a large ensemble cast but centers on three primary story arcs. The first story arc centers on the Iron Throne of the Seven Kingdoms and follows a web of alliances and conflicts among the dynastic noble families either vying to claim the throne or fighting for independence from the throne. The second story arc focuses on the last descendant of the realm's deposed ruling dynasty, exiled and plotting a return to the throne. The third story arc centers on the longstanding brotherhood charged with defending the realm against the ancient threats of the fierce peoples and legendary creatures that lie far north, and an impending winter that threatens the realm.
Game of Thrones has attracted record viewership on HBO and has a broad, active, international fan base. It has been acclaimed by critics, particularly for its acting, complex characters, story, scope, and production values, although its frequent use of nudity and violence (including sexual violence) has been criticized. The series has received 47 Primetime Emmy Awards, including Outstanding Drama Series in 2015, 2016, and 2018, more than any other primetime scripted television series. Its other awards and nominations include three Hugo Awards for Best Dramatic Presentation (2012 to 2014), a 2011 Peabody Award, and five nominations for the Golden Globe Award for Best Television Series Drama (2012 and 2015 to 2018).
"""
        IMDBLink='IMDb page'
        Link='https:www.imdb.com/title/tt0944947'
        return render_template('pageBase.html', BackgroundColour=bg, Title=Title, Programme=Programme, Channel=Channel, ImgSrc=ImgSrc, Rating=Rating, Section1=Section1, IMDBLink=IMDBLink, Link=Link, ImagePage=ImagePage), 200






@app.route('/categories/a-z-list/the-jeremy-kyle-show')
@app.route('/categories/ratings/the-jeremy-kyle-show')
@app.route('/categories/genres/talkshow/the-jeremy-kyle-show')
def programmejezza():
	bg='#286bb7'
        Title='The Jeremy Kyle Show'
        Programme='The Jeremy Kyle Show'
        Channel='ITV1, ITV2, 5:00am - 5:50pm'
        ImgSrc='/static/Jezza.jpg'
	ImagePage='http://set09103.napier.ac.uk:9147/the-jeremy-kyle-show/Jezza.jpg'
        Rating='4.1/10 IMDb Rating'
	Section1="""The Jeremy Kyle Show is a British tabloid talk show presented by Jeremy Kyle. It has been broadcast on ITV since 4 July 2005. The show is produced by ITV Studios and is broadcast each weekday at 09:25. The show first appeared as a replacement for Trisha Goddard's chat show, which was moved to Five.
The show is based on confrontations in which guests attempt to resolve issues with others that are significant in their lives. These issues are often related to: family relationships; romantic relationships; sex; drugs; and alcohol, among other issues. Frequently, guests display strong emotions such as anger and distress on the show, and Kyle often verbally chastises those that he feels have acted in morally dubious or irresponsible ways, while strongly emphasising the importance of traditional family values. This has led to severe criticism of the show, with one Manchester District Judge calling it "human bear-baiting" during a prosecution after guests had been involved in a violent incident on the show. 
The show also features psychotherapist Graham Stanier, who helps Kyle during the show and assists guests further after they are on air. Dr. Arun Ghosh also occasionally appears with medical help, often aiding people with drug or alcohol problems. A lie detector is used to determine the veracity of guests' claims, despite scientific research demonstrating the inefficacy of lie detectors. Allegations have been made by people involved with the show that guests commonly have mental illnesses and are mislead by researchers, with many former guests reporting of poor treatment; ITV spokespeople have disputed many of these claims.
The show's 1,000th episode was aired on 18 March 2010. In 2012, the show returned from its Christmas break with a new set. In 2017, the show returned from its Easter break with a new set and a refreshed look. 
"""       
	IMDBLink='IMDb page'
        Link='https:www.imdb.com/title/tt0492430'
        return render_template('pageBase.html', BackgroundColour=bg, Title=Title, Programme=Programme, Channel=Channel, ImgSrc=ImgSrc, Rating=Rating, Section1=Section1, IMDBLink=IMDBLink, Link=Link, ImagePage=ImagePage), 200





@app.route('/categories/a-z-list/x-factor')
@app.route('/categories/ratings/x-factor')
@app.route('/categories/genres/gameshow/x-factor')
def programmexfactor():
	bg='#ba1010'
        Title='X Factor'
        Programme='X Factor'
        Channel='ITV 8pm'
        ImgSrc='/static/Xfactor.jpg'
	ImagePage='http://set09103.napier.ac.uk:9147/x-factor/Xfactor.jpg'
        Rating='4.5/10 IMDb Rating'
        Section1="""The X Factor is a British reality television music competition to find new singing talent. The contestants are aspiring singers drawn from public auditions. Created by Simon Cowell, the show began in 2004 and has since aired annually from August/September until December. The show is produced by Fremantle's Thames (previously Talkback Thames) and Cowell's production company Syco Entertainment. It is broadcast on the ITV network in the UK and simulcast on TV3 in Ireland. "X Factor" refers to the undefinable "something" that makes for star quality. The series consists of auditions, bootcamp, judges' houses, several weeks of live shows, semi-finals and the final. The series had a spin-off behind-the-scenes show called The Xtra Factor, which aired directly after the main show on ITV2. This lasted for the first thirteen series, when it was cancelled by ITV in January 2017. It is replaced by an online spin-off show Xtra Bites exclusively on the ITV Hub. The first three series were presented by Kate Thornton, then from series four to eleven, the show was presented by Dermot O'Leary. Series 12 was presented by Caroline Flack and Olly Murs with O'Leary returning for series 13 onwards.
The show is split into different stages, following the contestants from auditions through to the final. In the original televised audition stage of the show, contestants sang in an audition room in front of just the judges, but from the sixth series onwards auditionees sing on a stage in front of the judges and a live audience. In series 10 and 11, both auditions formats were used. In series 12, the room auditions were scrapped, leaving just the arena auditions. The room auditions were revived in series 13, and no arena auditions followed. Successful auditionees go through to "bootcamp" and then to "judges' houses", where judges narrow down the acts in their category down to three or four acts to mentor for the live shows, where the public vote for their favourite acts following weekly live performances by the contestants."""
        IMDBLink='IMDb page'
        Link='https:www.imdb.com/title/tt0423776'
        return render_template('pageBase.html', BackgroundColour=bg, Title=Title, Programme=Programme, Channel=Channel, ImgSrc=ImgSrc, Rating=Rating, Section1=Section1, IMDBLink=IMDBLink, Link=Link, ImagePage=ImagePage), 200


@app.route('/24-hours-in-a&e/24H.jpg')
def img24():
	ImgSrc='/static/24H.jpg'
	return render_template('imageBase.html', ImgSrc=ImgSrc)

@app.route('/the-apprentice/Apprentice.jpg')
def inherits_fourteen():
	ImgSrc='/static/Apprentice.jpg'
	return render_template('imageBase.html', ImgSrc=ImgSrc)


@app.route('/bbc-news/bbc.jpg')
def imgbbc():
	ImgSrc='/static/BBC.jpg'
	return render_template('imageBase.html', ImgSrc=ImgSrc)


@app.route('/big-brother/BigBro.jpg')
def imgbb():
	ImgSrc='/static/BigBro.jpg'
	return render_template('imageBase.html', ImgSrc=ImgSrc)


@app.route('/breaking-bad/Breaking.jpg')
def imgbreaking():
	ImgSrc='/static/Breaking.jpg'
	return render_template('imageBase.html', ImgSrc=ImgSrc)


@app.route('/casualty/Casualty.jpg')
def imgcasualty():
	ImgSrc='/static/Casualty.jpg'
	return render_template('imageBase.html', ImgSrc=ImgSrc)


@app.route('/friends/friends.jpg')
def imgfriends():
	ImgSrc='/static/friends.jpg'
	return render_template('imageBase.html', ImgSrc=ImgSrc)


@app.route('/game-of-thrones/Got.jpg')
def imggot():
	ImgSrc='/static/Got.jpg'
	return render_template('imageBase.html', ImgSrc=ImgSrc)


@app.route('/the-jeremy-kyle-show/Jezza.jpg')
def imgjezza():
	ImgSrc='/static/Jezza.jpg'
	return render_template('imageBase.html', ImgSrc=ImgSrc)


@app.route('/x-factor/Xfactor.jpg')
def imgxfactor():
	ImgSrc='/static/Xfactor.jpg'
	return render_template('imageBase.html', ImgSrc=ImgSrc)



if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
