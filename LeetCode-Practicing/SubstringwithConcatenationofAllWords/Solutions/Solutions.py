#O(n^3) solution in the worst case, short write but very long runtime.
def findSubstring(s, words):
    res = []
    if len(s) == 1 and len(words) == 1: #edge case
        if s == words[0]:
            return [0]
    if len(words)*len(words[0]) > len(s): #edge case
        return[]
    chunkLen = len(words) * len(words[0])
    chunks = []
    for c in range (0, (len(s) - chunkLen + 1)):
        chunks.append([s[c :  c + chunkLen],c])
    for chunk in chunks:
        words2 = []
        for word in words:
            words2.append(word)
        for i in range (0, chunkLen -len(words[0])+1, len(words[0])):
            for word in words2:
                if chunk[0][i : i + len(word)] == word:
                    chunk[0] = chunk[0].replace(word ," "*len(word) ,1)
                    words2.remove(word)
                if len(words2) == 0 or words2[0] == chunk[0].replace(" ",""):
                    res.append(chunk[1])  
    res = list(dict.fromkeys(res))    
    return res
    



#O(n^2) solution in the worst case, lomg write but in good runtime.
def findSubstring2(s, words):
        
        words_d= {w:idx for idx, w in enumerate(words)}
        
        def to_id_arr(src, w_len= len(words[0])):
            res= list()
            for st in range(0, len(src), w_len):
                ed= st+w_len
                sub_src= src[st:ed]
                if sub_src in words_d:
                    res.append(words_d[sub_src])
                else:
                    res.append(None)
            return res
        
        req_d= dict()
        for x in words:
            key= words_d[x]
            if key not in req_d: req_d[key]=0
            req_d[key]+=1
        
        def solve(id_arr, shift=0, wrds_cnt= len(words)):
            res= list()
            d= dict()
            for v_idx, v in enumerate(id_arr):
                if v is not None:
                    if v not in d:
                        d[v]=0
                    d[v]+=1
                rm_idx= v_idx-wrds_cnt
                if rm_idx<0 or id_arr[rm_idx] is None:
                    pass
                else:
                    rm_word= id_arr[rm_idx]
                    d[rm_word]-=1
                    if d[rm_word]==0:
                        del d[rm_word]
                if d==req_d:
                    res.append((v_idx-wrds_cnt+1)*len(words[0])+shift)
            return res
        
        
        res= list()
        for shift in range(len(words[0])):
            id_arr= to_id_arr(s[shift:])
            c_res= solve(id_arr, shift=shift)
            res.extend(c_res)
        return res




def main():
    s = "ejwwmybnorgshugzmoxopwuvshlcwasclobxmckcvtxfndeztdqiakfusswqsovdfwatanwxgtctyjvsmlcoxijrahivwfybbbudosawnfpmomgczirzscqvlaqhfqkithlhbodptvdhjljltckogcjsdbbktotnxgwyuapnxuwgfirbmdrvgapldsvwgqjfxggtixjhshnzphcemtzsvodygbxpriwqockyavfscvtsewyqpxlnnqnvrkmjtjbjllilinflkbfoxdhocsbpirmcbznuioevcojkdqvoraeqdlhffkwqbjsdkfxstdpxryixrdligpzldgtiqryuasxmxwgtcwsvwasngdwovxzafuixmjrobqbbnhwpdokcpfpxinlfmkfrfqrtzkhabidqszhxorzfypcjcnopzwigmbznmjnpttflsmjifknezrneedvgzfmnhoavxqksjreddpmibbodtbhzfehgluuukupjmbbvshzxyniaowdjamlfssndojyyephstlonsplrettspwepipwcjmfyvfybxiuqtkdlzqedjxxbvdsfurhedneauccrkyjfiptjfxmpxlssrkyldfriuvjranikluqtjjcoiqffdxaukagphzycvjtvwdhhxzagkevvuccxccuoccdkbboymjtimdrmerspxpktsmrwrlkvpnhqrvpdekmtpdfuxzjwpvqjjhfaupylefbvbsbhdncsshmrhxoyuejenqgjheulkxjnqkwvzznriclrbzryfaeuqkfxrbldyusoeoldpbwadhrgijeplijcvqbormrqglgmzsprtmryvkeevlthvflsvognbxfjilwkdndyzwwxgdbeqwlldyezmkopktzugxgkklimhhjqkmuaifnodtpredhqygmedtqpezboimeuyyujfjxkdmbjpizpqltvgknnlodtbhnbhjkmuhwxvzgmkhbcvvadhnssbvneecglnqxhavhvxpkjxlluilzpysjcnwguyofnhfvhaceztoiscumkhociglkvispihvyoatxcxbeqsmluixgsliatukrecgoldmzfhwkgaqzsckonjuhxdhqztjfxstjvikdrhpyjfxbjjryslfpqoiphrwfjqqhaamrjbrsiovrxmqsyxhqmritjeauwqbwtpqcqhvyyssvfknfhxvtodpzipueixdbntdfcaeatyyainfpkclbgaaqrwwzwbcjwiqzkwzfuxfclmsxpdyvfbnwxjytnaejivivriamhgqsskqhnqeurttrfrmstrbeokzhuzvbfmwywohmgogyhzpmsdemugqkspsmoppwbnwabdmiruibwznqcuczculujfiavzwynsyqxmarjkshjhxobandwyzggjibjgzyaaqxorqxbkenscbveqbaociwmqxxyzvyblypeongzrttvwqzmrccwkzidyfbxcaypyquodcpwxkstbthuvjqgialhfmgjohzoxvdaxuywfqrgmyahhtpqtazbphmfoluliznftodyguesshcacrsvutylalqrykehjuofisdookjhrljvedsywrlyccpaowjaqyfaqioesxnlkwgpbznzszyudpwrlgrdgwdyhucztsneqttsuirmjriohhgunzatyfrfzvgvptbgpwajgtysligupoqeoqxoyqtzozufvvlktnvahvsseymtpeyfvxttqosgpplkmxwgmsgtpantazppgnubmpwcdqkvhwfuvcahwibniohiqyywnuzzmxeppokxksrfwrpuzqhjgqryorwboxdauhrkxehiwaputeouwxdfoudcoagcxjcuqvenznxxnprgvhasffxtzaxpcfrcovwgrcwqptoekhmgpoywtxruxokcubekzcrqengviwbtgnzvdzrwwkqvacxwgdhffyvjldgvchoiwnfzoyvkiogisdfyjmfomcazigukqlumyzmnzjzhzfpslwsukykwckvktswjdqxdrlsqvsxwxpqkljeyjpulbswwmuhplfueqnvnhukgjarxlxvwmriqjgmxawmndhsvwnjdjvjtxcsjapfogpesxtpypenunfpjuyoevzztctecilqqbxkaqcyhiobvtqgqruumvvhxolbyzsqcrdchhdqprtkkjsccowrjtyjjmkhleanvfpemuublnnyzfabtxsestncfalqenfcswgerbfcqsapzdtscnzugmwlmidtxkvqhbuaecevwhmwkfqmvpgbefpqpsjmdecmixmmbsjxzwvjdmxydechlraajjmoqpcyoqmrjwoiumuzatydzcnktnkeyztoqvogodxxznhvzduzxudwwqhpftwdspuimioanlzobhjakgajafgzxpqckmhdbbnqmcszpuoqbztnftzgahhxwxbgkilnmzfydyxusnnvngksbjabqjaohdvrniezhmxmkxhemwbbclwdxwgngicplzgajmaryzfkyoqlkrmmfirchzrphveuwmvgaxzbwenvteifxuuefnimnadwxhruvoavlzyhfmeasmgrjawongccgfbgoualiaivbhcgvjjnxpggrewglalthmzvgziobrjeanlvyukwlscexbkibvdjhdgnepdiimmkcxhattwglbkicvsfswocbvphmtpwhcgjbnmxgidtlqcnnwtfujhvgzdussqbwynylzvtjapvqtidpdjkpshvrmqlhindhabubyokzdfrwqvnvgzkyhistydagsgnujiviyijdnabfxqbdqnexvwsvzvcsbrmkbkuzsdehghndyqjodnnblfwmaygdstotfkvxozgwhtbhlkvrzismnozqpfthajafuxekzlgigjpsukjvsdihrjzgovnreqwapdkoqswyclqyvbvpedzyoyedvuuamscbxnqnfmmjyehvidnoimmxmtcinwkbqmcobubjjpshucechrqrffqsyscnqoohcsxenypyqhfklloudgmklcejvgynwouzhtfwuuukdbwpmkjrqxeeaipxrokncholathupdetgaktmvmftqjvzyssocftjwemroghrncynmtchhhcaqxbqpthuaafwgrouaxonzocljeuslzsdwvuoodipdpnlhdihaywzmymxdjrqikughquwtenyucjdgrmipiidiwclhuepgyynoslhzahtdqwliktzsddaahohbszhqxxgripqlwlomjbwtuynydoakejmwkvojuwbfltqjfgxqhwkduzbxpdhtpvrzrfjndmsqfizmqxdxtpbpoemekvxzrrakwjxcxqsdasptruqmjtbaapgmkfnbwnlvzlxwdpzfjryanrmzmpzoefapmnsjdgecrdywsabctaegttffigupnwgakylngrrxurtotxqmzxvsqazajvrwsxyeyjteakeudzjxwbjvagnsjntskmocmpgkybqbnwvrwgoskzqkgffpsyhfmxhymqinrbohxlytsmoeleqrjvievpjipsgdkrqeuglrsjnmvdsihicsgkybcjltcswolpsfxdypmlbjotuxewskisnmczfgreuevnjssjifvlqlhkllifxrxkdbjlhcpegmtrelbosyajljvwwedtxbdccpnmreqaqjrxwulpunagwxesbilalrdniqbzxrbpcvmzpyqklsskpwctgqtrjwhrpisocwderqfiqxsdpkphjsapkvhvsqojyixaechvuoemmyqdlfkuzmlliugckuljfkljoshjhlvvlnywvjswvekfyqhjnsusefdtakejxbejrchoncklguqgnyrcslwztbstmycjziuskegagtlonducdogwbevugppsptdqbajmepmmizaycwcgmjeopbivsyphtvxvvgjbyxpgwpganjiaumojpyhhywosrmnouwpstgbrvhtlqcnmqbygbfnabesvshjmdbhyhirfrkqkmfwdgujhzyjdcbyuijjnkqluaczrnrbbwaeeupnwqzbsazplkyaxqorqsshhlljjlpphhedxdepgfgrqerpuhgmaawhnhqwsgnznrfmxjbdrkwjopylxezxgvetcvrwdewsxdeumhzfrvoilmvksuhyqltuimrnsphqslmgvmmojawwptghonigbdclqtbikiacwpjrbxhmzejozpypfixglatdvuogdoizdtsgsztsfcihtgwyqugeuahpuvvzmgarbsyuutmbxuisdfrvbxzxzhmuektssuktoknkfbmcwwubbnwenybmfqglaceuyqnoadzfenjcjfdlvcpiatuhjdujhaffqsvqvuxchgerokejovrqonxxstibunikiedfyahijobxyhimebctobsjudkqstbcxgixgrhpfiofpwruzvpqyjzvollheoldutddnksutjakhtghpxxnjykxjwgqmsvhnykclexepxqxqzghwfxfdhfmflesfabvanxlrurjtigkjotftqnwyskffpxlragrnfffawqtgyfpmzxfpkdpenxlewyxxgrkmwrmshhzfnorolyfxbvdrspxqnxnuoygkruczddgssygfymdcjgvdxutlrhffhnpyjuxmxefrelxezcgikdliyhvpocvvpkvagvmezrxffujeysplvavtjqjxsgujqsjznxforctwzecxyrkwufpdxadrgzczrnyelfschnagucguuqqqwitviynrypsrdswqxqsegulcwrwsjnihxedfcqychqumiscfkwmqqxunqrfbgqjdwmkyelbldxympctbzfupeocwhkypchuyvhybsbmvymjppfrqmlfrbkpjwpyyytytawuuyjrwxboogfessmltwdcssdqtwomymjskujjtmxiueopwacrwfuqazitvyhvlspvoaeipdsjhgyfjbxhityisidnhlksfznubucqxwaheamndjxmcxwufajmnveuwuoyosqnoqwvtjkwuhkzghvmjhawcfszbhzrbpgsidnbmxxihihnrfbamcyojqpkzodbejtmmipahojoysepzhpljpaugrghgjimtdahnpivdtlcnptnxjyiaafislqavamqgmxtdfoiaakorebqpbbpegawrqymqkewycsdjglkiwaacdqterkixkgraedtqirqmjtvsfhadhafktyrmkzmvidxmisfskvevpcnujqxrqedleuyowkjgphsxzzqlvujkwwgiodbfjesnbsbzcnftuzrvzjjudsgcqmmfpnmyrenuxotbbyvxyovzxgtcyzgqnsvcfhczoptnfnojnlinbfmylhdlijcvcxzjhdixuckaralemvsnbgooorayceuedtomzyjtctvtwgyiesxhynvogxnjdjphcftbefxgasawzagfugmuthjahylkhatlgpnkuksuesrduxkodwjzgubpsmzzmvkskzeglxaqrrvmrgcwcnvkhwzbibaxwnriowoavosminabvfxastkcrkdclgzjvqrjofjjvbyfragofeoazzeqljuypthkmywaffmcjkickqqsuhsviyovhitxeajqahshpejaqtcdkuvgdpclnsguabtgbfwdmrmbvydorfrbcokfdmtsgboidkpgpnmdeyhawkqqshtwxdbarwuxykgduxjlkxppwyruihkcqgynjcpbylayvgdqfpbqmshksyfbhrfxxemhgbkgmkhjtkzyzdqmxxwqvdtevyducpdksntgyaqtkrrkwiyuhukfadjvdnrievszilfinxbyrvknfihmetreydbcstkwoexwsfhfekfvfplmxszcosgovisnbemrjlndqwkvhqsofdbdychmupcsxvhazvrihhnxfyumonbvqeyoghccxfuwacxzxqkezxefxarnnujgyjugrzjoefmghjfhcrnbrtgouaehwnnxwkdplodpuqxdbemfwahptpfppjzowoltyqijfoabgzejerpatwponuefgdtcrgxswiddygeeflpjeelzccnsztxfyqhqyhkuppapvgvdtkmxraytcolbhkiiasaazkvqzvfxbaaxkoudovxrjkusxdazxaawmvoostlvvnsfbpjqkijvudpriqrfsrdfortimgdhtypunakzituezjyhbrpuksbamuiycngvlvpyvczfxvlwhjgicvempfobbwadkiavdswyuxdttoqaaykctprkwfmyeodowglzyjzuhencufcwdobydslazxadnftllhmjslfbrtdlahkgwlebdpdeofidldoymakfnpgekmsltcrrnxvspywfggjrmxryybdltmsfykstmlnzjitaipfoyohkmzimcozxardydxtpjgquoluzbznzqvlewtqyhryjldjoadgjlyfckzbnbootlzxhupieggntjxilcqxnocpyesnhjbauaxcvmkzusmodlyonoldequfunsbwudquaurogsiyhydswsimflrvfwruouskxjfzfynmrymyyqsvkajpnanvyepnzixyteyafnmwnbwmtojdpsucthxtopgpxgnsmnsrdhpskledapiricvdmtwaifrhnebzuttzckroywranbrvgmashxurelyrrbslxnmzyeowchwpjplrdnjlkfcoqdhheavbnhdlltjpahflwscafnnsspikuqszqpcdyfrkaabdigogatgiitadlinfyhgowjuvqlhrniuvrketfmboibttkgakohbmsvhigqztbvrsgxlnjndrqwmcdnntwofojpyrhamivfcdcotodwhvtuyyjlthbaxmrvfzxrhvzkydartfqbalxyjilepmemawjfxhzecyqcdswxxmaaxxyifmouauibstgpcfwgfmjlfhketkeshfcorqirmssfnbuqiqwqfhbmol"
    words = ["toiscumkhociglkvispihvyoatxcx","ndojyyephstlonsplrettspwepipw","yzfkyoqlkrmmfirchzrphveuwmvga","mxxihihnrfbamcyojqpkzodbejtmm","fenjcjfdlvcpiatuhjdujhaffqsvq","ehghndyqjodnnblfwmaygdstotfkv","heoldutddnksutjakhtghpxxnjykx","cvrwdewsxdeumhzfrvoilmvksuhyq","ftqjvzyssocftjwemroghrncynmtc","idiwclhuepgyynoslhzahtdqwlikt","eurttrfrmstrbeokzhuzvbfmwywoh","jxlluilzpysjcnwguyofnhfvhacez","uskegagtlonducdogwbevugppsptd","xmcxwufajmnveuwuoyosqnoqwvtjk","wolpsfxdypmlbjotuxewskisnmczf","fjryanrmzmpzoefapmnsjdgecrdyw","jgmxawmndhsvwnjdjvjtxcsjapfog","wuhkzghvmjhawcfszbhzrbpgsidnb","yelbldxympctbzfupeocwhkypchuy","vzduzxudwwqhpftwdspuimioanlzo","bdpdeofidldoymakfnpgekmsltcrr","fmyeodowglzyjzuhencufcwdobyds","dhtypunakzituezjyhbrpuksbamui","bdmiruibwznqcuczculujfiavzwyn","eudzjxwbjvagnsjntskmocmpgkybq","tuynydoakejmwkvojuwbfltqjfgxq","psrdswqxqsegulcwrwsjnihxedfcq","cokfdmtsgboidkpgpnmdeyhawkqqs","fujhvgzdussqbwynylzvtjapvqtid","rqeuglrsjnmvdsihicsgkybcjltcs","vhybsbmvymjppfrqmlfrbkpjwpyyy","aukagphzycvjtvwdhhxzagkevvucc","hwkduzbxpdhtpvrzrfjndmsqfizmq","ywnuzzmxeppokxksrfwrpuzqhjgqr","qbajmepmmizaycwcgmjeopbivsyph","uamscbxnqnfmmjyehvidnoimmxmtc","nxvspywfggjrmxryybdltmsfykstm","amrjbrsiovrxmqsyxhqmritjeauwq","yorwboxdauhrkxehiwaputeouwxdf","qkewycsdjglkiwaacdqterkixkgra","ycngvlvpyvczfxvlwhjgicvempfob","jgphsxzzqlvujkwwgiodbfjesnbsb","mkxhemwbbclwdxwgngicplzgajmar","mryvkeevlthvflsvognbxfjilwkdn","mezrxffujeysplvavtjqjxsgujqsj","rtotxqmzxvsqazajvrwsxyeyjteak","sabctaegttffigupnwgakylngrrxu","xccuoccdkbboymjtimdrmerspxpkt","xusnnvngksbjabqjaohdvrniezhmx","oyuejenqgjheulkxjnqkwvzznricl","mxszcosgovisnbemrjlndqwkvhqso","wsgnznrfmxjbdrkwjopylxezxgvet","dxmisfskvevpcnujqxrqedleuyowk","dhrgijeplijcvqbormrqglgmzsprt","vuxchgerokejovrqonxxstibuniki","lumyzmnzjzhzfpslwsukykwckvkts","inwkbqmcobubjjpshucechrqrffqs","ywtxruxokcubekzcrqengviwbtgnz","ccpnmreqaqjrxwulpunagwxesbila","pesxtpypenunfpjuyoevzztctecil","sygfymdcjgvdxutlrhffhnpyjuxmx","uisdfrvbxzxzhmuektssuktoknkfb","cejvgynwouzhtfwuuukdbwpmkjrqx","oudcoagcxjcuqvenznxxnprgvhasf","sxnlkwgpbznzszyudpwrlgrdgwdyh","qqbxkaqcyhiobvtqgqruumvvhxolb","mkhleanvfpemuublnnyzfabtxsest","bibaxwnriowoavosminabvfxastkc","bcxgixgrhpfiofpwruzvpqyjzvoll","lzccnsztxfyqhqyhkuppapvgvdtkm","pdjkpshvrmqlhindhabubyokzdfrw","qbbnhwpdokcpfpxinlfmkfrfqrtzk","rnyelfschnagucguuqqqwitviynry","qtrjwhrpisocwderqfiqxsdpkphjs","vxttqosgpplkmxwgmsgtpantazppg","tyisidnhlksfznubucqxwaheamndj","kgaqzsckonjuhxdhqztjfxstjvikd","jeuslzsdwvuoodipdpnlhdihaywzm","vdzrwwkqvacxwgdhffyvjldgvchoi","cftbefxgasawzagfugmuthjahylkh","xraytcolbhkiiasaazkvqzvfxbaax","oyqtzozufvvlktnvahvsseymtpeyf","rnnujgyjugrzjoefmghjfhcrnbrtg","rfzvgvptbgpwajgtysligupoqeoqx","igbdclqtbikiacwpjrbxhmzejozpy","dyzwwxgdbeqwlldyezmkopktzugxg","hmetreydbcstkwoexwsfhfekfvfpl","zcnftuzrvzjjudsgcqmmfpnmyrenu","zzmvkskzeglxaqrrvmrgcwcnvkhwz","vjswvekfyqhjnsusefdtakejxbejr","rwwzwbcjwiqzkwzfuxfclmsxpdyvf","fdbdychmupcsxvhazvrihhnxfyumo","vdtevyducpdksntgyaqtkrrkwiyuh","nbvqeyoghccxfuwacxzxqkezxefxa","vpgbefpqpsjmdecmixmmbsjxzwvjd","jwgqmsvhnykclexepxqxqzghwfxfd","olyfxbvdrspxqnxnuoygkruczddgs","qgmxtdfoiaakorebqpbbpegawrqym","liaivbhcgvjjnxpggrewglalthmzv","choncklguqgnyrcslwztbstmycjzi","fpkdpenxlewyxxgrkmwrmshhzfnor","hhhcaqxbqpthuaafwgrouaxonzocl","ipahojoysepzhpljpaugrghgjimtd","wosrmnouwpstgbrvhtlqcnmqbygbf","nwyskffpxlragrnfffawqtgyfpmzx","bcvvadhnssbvneecglnqxhavhvxpk","hoavxqksjreddpmibbodtbhzfehgl","lazxadnftllhmjslfbrtdlahkgwle","uuukupjmbbvshzxyniaowdjamlfss","tpqtazbphmfoluliznftodyguessh","ychqumiscfkwmqqxunqrfbgqjdwmk","rkdclgzjvqrjofjjvbyfragofeoaz","pphhedxdepgfgrqerpuhgmaawhnhq","cacrsvutylalqrykehjuofisdookj","kyldfriuvjranikluqtjjcoiqffdx","bnwvrwgoskzqkgffpsyhfmxhymqin","uzmlliugckuljfkljoshjhlvvlnyw","abfxqbdqnexvwsvzvcsbrmkbkuzsd","xotbbyvxyovzxgtcyzgqnsvcfhczo","bwtpqcqhvyyssvfknfhxvtodpzipu","nsfbpjqkijvudpriqrfsrdfortimg","tgwyqugeuahpuvvzmgarbsyuutmbx","upnwqzbsazplkyaxqorqsshhlljjl","edfyahijobxyhimebctobsjudkqst","ialhfmgjohzoxvdaxuywfqrgmyahh","jlhcpegmtrelbosyajljvwwedtxbd","tpfppjzowoltyqijfoabgzejerpat","mgogyhzpmsdemugqkspsmoppwbnwa","nubmpwcdqkvhwfuvcahwibniohiqy","ukfadjvdnrievszilfinxbyrvknfi","dgnepdiimmkcxhattwglbkicvsfsw","syqxmarjkshjhxobandwyzggjibjg","bnwxjytnaejivivriamhgqsskqhnq","hzyjdcbyuijjnkqluaczrnrbbwaee","yscnqoohcsxenypyqhfklloudgmkl","habidqszhxorzfypcjcnopzwigmbz","wjdqxdrlsqvsxwxpqkljeyjpulbsw","tytawuuyjrwxboogfessmltwdcssd","pfixglatdvuogdoizdtsgsztsfcih","apkvhvsqojyixaechvuoemmyqdlfk","ouaehwnnxwkdplodpuqxdbemfwahp","ixuckaralemvsnbgooorayceuedto","ymxdjrqikughquwtenyucjdgrmipi","smrwrlkvpnhqrvpdekmtpdfuxzjwp","bhjakgajafgzxpqckmhdbbnqmcszp","beqsmluixgsliatukrecgoldmzfhw","greuevnjssjifvlqlhkllifxrxkdb","yzsqcrdchhdqprtkkjsccowrjtyjj","sviyovhitxeajqahshpejaqtcdkuv","qtwomymjskujjtmxiueopwacrwfuq","mzyjtctvtwgyiesxhynvogxnjdjph","dyfbxcaypyquodcpwxkstbthuvjqg","hfmflesfabvanxlrurjtigkjotftq","mxydechlraajjmoqpcyoqmrjwoium","nabesvshjmdbhyhirfrkqkmfwdguj","bhrfxxemhgbkgmkhjtkzyzdqmxxwq","gziobrjeanlvyukwlscexbkibvdjh","mcwwubbnwenybmfqglaceuyqnoadz","xyzvyblypeongzrttvwqzmrccwkzi","ncfalqenfcswgerbfcqsapzdtscnz","dtqpezboimeuyyujfjxkdmbjpizpq","wmuhplfueqnvnhukgjarxlxvwmriq","qwapdkoqswyclqyvbvpedzyoyedvu","uoqbztnftzgahhxwxbgkilnmzfydy","zsddaahohbszhqxxgripqlwlomjbw","bwadkiavdswyuxdttoqaaykctprkw","eixdbntdfcaeatyyainfpkclbgaaq","nmjnpttflsmjifknezrneedvgzfmn","avlzyhfmeasmgrjawongccgfbgoua","kklimhhjqkmuaifnodtpredhqygme","xzbwenvteifxuuefnimnadwxhruvo","ugmwlmidtxkvqhbuaecevwhmwkfqm","rhpyjfxbjjryslfpqoiphrwfjqqha","eeaipxrokncholathupdetgaktmvm","ltuimrnsphqslmgvmmojawwptghon","azitvyhvlspvoaeipdsjhgyfjbxhi","efrelxezcgikdliyhvpocvvpkvagv","znxforctwzecxyrkwufpdxadrgzcz","kcqgynjcpbylayvgdqfpbqmshksyf","hrljvedsywrlyccpaowjaqyfaqioe","cjmfyvfybxiuqtkdlzqedjxxbvdsf","zeqljuypthkmywaffmcjkickqqsuh","wnfzoyvkiogisdfyjmfomcazigukq","zyaaqxorqxbkenscbveqbaociwmqx","ahnpivdtlcnptnxjyiaafislqavam","edtqirqmjtvsfhadhafktyrmkzmvi","wponuefgdtcrgxswiddygeeflpjee","xozgwhtbhlkvrzismnozqpfthajaf","ptnfnojnlinbfmylhdlijcvcxzjhd","uxekzlgigjpsukjvsdihrjzgovnre","rbohxlytsmoeleqrjvievpjipsgdk","fxtzaxpcfrcovwgrcwqptoekhmgpo","tvxvvgjbyxpgwpganjiaumojpyhhy","vqjjhfaupylefbvbsbhdncsshmrhx","urhedneauccrkyjfiptjfxmpxlssr","ltvgknnlodtbhnbhjkmuhwxvzgmkh","ucztsneqttsuirmjriohhgunzatyf","rbzryfaeuqkfxrbldyusoeoldpbwa","atlgpnkuksuesrduxkodwjzgubpsm","lrdniqbzxrbpcvmzpyqklsskpwctg","qvnvgzkyhistydagsgnujiviyijdn","uzatydzcnktnkeyztoqvogodxxznh","ocbvphmtpwhcgjbnmxgidtlqcnnwt","koudovxrjkusxdazxaawmvoostlvv","ptruqmjtbaapgmkfnbwnlvzlxwdpz","xdxtpbpoemekvxzrrakwjxcxqsdas","gdpclnsguabtgbfwdmrmbvydorfrb","htwxdbarwuxykgduxjlkxppwyruih"]
    print("findSubstring1/findSubstring2(s, words)") #Choose one of the solutions and run
    
    
        
    


if __name__ == "__main__":
    main()


