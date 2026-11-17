# Rebuilds index.html. Edit the NOV data below (status, url, date), then run: python build.py
import html as H
BC="https://app.basecamp.com/4238785/buckets/"
GS="https://docs.google.com/spreadsheets/d/"
# status: Planned / Written / Scheduled / Live ; index: Not checked / Requested / Indexed / -
CL=[
("Bennies Cafe",3,"49108196/documents/10364294386#__recording_10506033364","49108196/todolists/10516601708","1agTU8rku8-RWUqRkMz2S-0quZgTb0tOlQPAtyErMykk",[
 ("What Is Eggs Benedict, and What Goes on a Bennie at Our Monument Cafe?","what is eggs benedict","Nov 20","Planned","","-"),
 ("What Is a Dirty Chai Latte, and What Is in It?","what is a dirty chai","Nov 24","Planned","","-"),
 ("What Is a London Fog Drink, and What Is in It?","what is a london fog","Nov 30","Planned","","-")]),
("ClimateAlignmentHVACR",4,"48270650/documents/10410874315#__recording_10506030881","48270650/todolists/10516595868","1GUjaUnUKq7ZDAc8HHfwA4uMwULnG5GEdeIGSrR-39nM",[
 ("How Many Years Should an HVAC Last in Arvada?","how long does a commercial rooftop unit last","Nov 11","Live","https://climatealignmenthvacr.com/blog/how-many-years-should-a-commercial-rooftop-unit-last/","Not checked"),
 ("Why Is My Walk-In Cooler Not Cooling in Denver?","walk in cooler not cooling","Nov 19","Planned","","-"),
 ("Why Is My Commercial Ice Machine Not Making Ice in Denver?","commercial ice machine not making ice","Nov 24","Planned","","-"),
 ("What Temperature Should a Walk-In Cooler Be in Denver?","walk in cooler temperature","Nov 30","Planned","","-")]),
("ExcavatingNJ",4,"48270034/documents/10410875368#__recording_10506032140","48270034/todolists/10516598342","1nr-38Ydeu_t5SC9bPaUVyio_V1f915HmVFJe8bb_4MY",[
 ("How Many Years Will a Septic System Last in Wantage?","how long does a septic system last","Nov 11","Live","https://excavatingnj.com/blog/how-many-years-will-a-septic-system-last/","Not checked"),
 ("How Does a Norweco Septic System Work in Wantage?","norweco singulair","Nov 12","Live","https://excavatingnj.com/blog/how-does-a-norweco-septic-system-work/","Not checked"),
 ("Cesspool vs Septic System: What Is the Difference and Do You Have to Replace One in NJ?","cesspool vs septic","Nov 19","Planned","","-"),
 ("Does Homeowners Insurance Cover Septic Line Repair in Sussex County, NJ?","does homeowners insurance cover septic system","Nov 24","Planned","","-")]),
("Nakhon Luang Thai Kitchen",3,"48399899/documents/10444667450#__recording_10506033628","48399899/todolists/10516539913","1m8o_YvyLhKYNc1Ws2CEIQYF8caIUO0a_iTt_-w9f2Gs",[
 ("Vegetarian Thai Food Colorado Springs","vegetarian thai food colorado springs","Nov 9","Live","https://nakhonluangthaicos.com/vegetarian-thai-food-colorado-springs/","Not checked"),
 ("Which Thai Dishes Are Typically Vegan in Colorado Springs, CO?","thai dishes typically vegan","Nov 10","Live","https://nakhonluangthaicos.com/vegan-thai-food-colorado-springs/","Not checked"),
 ("Is Duck Healthy? Colorado Springs Thai Guide","is duck healthy","Nov 20","Planned","","-")]),
("OaksDentistry",4,"48270608/documents/10410876659#__recording_10506031565","48270608/todolists/10516596854","16gVLpeddhrxYspBfy23QPnLhl0dk2ptzvl9VC-IngrU",[
 ("What to Do in a Dental Emergency When You Don't Have a Dentist in Calabasas","what to do in a dental emergency","Nov 12","Live","https://oaksdentistry.com/blog/dental-emergency-with-no-dentist/","Not checked"),
 ("How Do I Know If I Need a Dental Crown or a Filling in Calabasas?","dental crown vs filling","Nov 20","Planned","","-"),
 ("What Happens If I Don't Wear Invisalign for 22 Hours a Day in Calabasas?","invisalign 22 hours a day","Nov 25","Planned","","-"),
 ("Do I Need a Crown After a Root Canal in Calabasas?","do you need a crown after a root canal","Nov 30","Planned","","-")]),
("TrueBalancePainRelief",4,"48270991/documents/10410878913#__recording_10506032028","48270991/todolists/10516598157","1fzMOUdDcXTM48j52cBxR59lAVwaigP0KFpCyOuwFtGA",[
 ("How to Prepare for a Sports Massage in Aurora?","how to prepare for a sports massage","Nov 12","Live","https://truebalancepainrelief.com/sports-massage/how-to-prepare-for-a-sports-massage-aurora/","Not checked"),
 ("Does Posture Alignment Therapy Work in Aurora?","posture alignment therapy","Nov 20","Planned","","-"),
 ("Why Am I Sore After a Deep Tissue Massage in Aurora?","sore after deep tissue massage","Nov 24","Planned","","-"),
 ("Does Cupping Therapy Hurt, and How Long Do the Marks Last in Aurora?","does cupping hurt","Nov 30","Planned","","-")]),
]
COL={"Planned":"#9a9a9a","Written":"#b7791f","Scheduled":"#1f6feb","Live":"#2f855a"}
e=H.escape
top="";sec=""
for n,c,g,l,s,rows in CL:
    live=sum(1 for r in rows if r[3]=="Live")
    drafts=sum(1 for r in rows if r[3] in ("Written","Scheduled","Live"))
    def cell(k,tot,word):
        col='#2f855a' if k>=tot else ('#b7791f' if k else '#c53030')
        left=tot-k
        tail=f"<br><span class=x>{left} to {word}</span>" if left else "<br><span class=x>complete</span>"
        return f"<td><b style='color:{col};font-size:16px'>{k}/{tot}</b>{tail}</td>"
    top+=f"<tr><td><b>{e(n)}</b></td><td>{c} a month</td>"+cell(drafts,c,'draft')+cell(live,c,'publish')+f"<td><a href='{BC}{g}' target='_blank'>Brand guide comment</a></td><td><a href='{BC}{l}' target='_blank'>Blog per Month list</a></td><td><a href='{GS}{s}/edit' target='_blank'>Topic sheet</a></td></tr>\n"
    sec+=f"<h2>{e(n)} <span class=x>{live} of {len(rows)} live &middot; <a href='{GS}{s}/edit' target='_blank'>topic sheet</a></span></h2>\n<div style='overflow-x:auto'><table style='min-width:900px'><tr><th>#</th><th>Topic</th><th>Main keyword</th><th>Target date</th><th>Status</th><th>Live URL</th><th>Indexing</th></tr>\n"
    for i,(t,k,d,st,u,ix) in enumerate(rows,1):
        url=f"<a href='{e(u)}' target='_blank'>Open post</a>" if u else "-"
        sec+=f"<tr><td>{i}</td><td>{e(t)}</td><td>{e(k)}</td><td>{d}</td><td><span class=s style='background:{COL[st]}'>{st}</span></td><td>{url}</td><td>{ix}</td></tr>\n"
    sec+="</table></div>\n"
page=f"""<!doctype html><html><head><meta name="robots" content="noindex, nofollow, noarchive, nosnippet"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Magister blog tracker</title>
<style>body{{font-family:Inter,Segoe UI,Arial,sans-serif;margin:24px;color:#1a1a1a;background:#fff}}
h1{{font-size:22px;margin:0 0 6px}}h2{{font-size:17px;margin:26px 0 8px}}p{{margin:4px 0 14px;color:#444}}
table{{border-collapse:collapse;width:100%;font-size:14px}}th{{background:#1f2937;color:#fff;text-align:left;padding:9px}}
td{{padding:9px;border-bottom:1px solid #e3e3e3;vertical-align:top}}tr:nth-child(even) td{{background:#f6f8fa}}
.s{{color:#fff;padding:3px 8px;border-radius:10px;font-size:12px;white-space:nowrap}}.x{{color:#555;font-size:13px;font-weight:400}}
a{{color:#1f6feb}}</style></head><body>
<h1>Magister blog tracker</h1>
<p>Updated Nov 17, 2026. Blogs a month come from Beth's comment on each client's brand guide (from Dimi's Client Sheet). Open the topic sheet for every topic, keyword and status.</p>
<div style="overflow-x:auto"><table style="min-width:900px"><tr><th>Client</th><th>Blogs a month</th><th>November drafts</th><th>November published</th><th>Cadence source</th><th>Basecamp list</th><th>Schedule</th></tr>
{top}</table></div>
<h1 style="margin-top:34px">November 2026</h1>
<p>Each client's blogs for the month. Dates are the targets from the topic sheets until the WordPress schedule is confirmed. Status goes Planned, Written, Scheduled, Live. "Not checked" under Indexing means the post is live but its indexing has not been looked at yet.</p>
{sec}
</body></html>"""
open("index.html","w",encoding="utf-8").write(page)
