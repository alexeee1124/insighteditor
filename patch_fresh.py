import os, re, json

BASE_DIR = '/Users/barshan/.gemini/antigravity/scratch/instastudio-app'

print("Patching fresh InstaStudio files...")

# 1. Patch app-CNoYCIA1.js
app_path = os.path.join(BASE_DIR, 'assets/app-CNoYCIA1.js')
with open(app_path, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Replace pu component (the entire license key gate)
start_pu = app_js.find('const Dr="ig-access-activated";function pu({children:e}){')
end_pu = app_js.find('const Ct=u.forwardRef', start_pu)

if start_pu != -1 and end_pu != -1:
    pu_replacement = 'const Dr="ig-access-activated";function pu({children:e}){return s.jsx(s.Fragment,{children:e})}'
    app_js = app_js[:start_pu] + pu_replacement + app_js[end_pu:]
    print("✓ Patched pu wrapper in app-CNoYCIA1.js (License gate removed)")
else:
    print("! Could not find pu bounds in app-CNoYCIA1.js")

# Also patch logout in app-CNoYCIA1.js so it doesn't redirect to /login
app_js = app_js.replace(
    'c({to:"/login",replace:!0})',
    'c({to:"/app",replace:!0})'
)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(app_js)


# 2. Patch login-di5LDrAH.js
login_path = os.path.join(BASE_DIR, 'assets/login-di5LDrAH.js')
if os.path.exists(login_path):
    with open(login_path, 'r', encoding='utf-8') as f:
        login_js = f.read()
    
    # Make ee component immediately redirect to /app
    start_ee = login_js.find('function ee(){')
    end_ee = login_js.find('export{ee as component};', start_ee)
    if start_ee != -1 and end_ee != -1:
        ee_replacement = 'function ee(){t.useEffect(()=>{window.location.replace("/app")},[]);return null}'
        login_js = login_js[:start_ee] + ee_replacement + login_js[end_ee:]
        with open(login_path, 'w', encoding='utf-8') as f:
            f.write(login_js)
        print("✓ Patched ee component in login-di5LDrAH.js (Instant redirect)")


# 3. Patch index-NM4phaV4.js (Default profile to barshaann)
idx_path = os.path.join(BASE_DIR, 'assets/index-NM4phaV4.js')
with open(idx_path, 'r', encoding='utf-8') as f:
    idx_js = f.read()

barshaann_profile_code = '''qs={profile:{username:"barshaann",displayName:"Barshan",avatar:"/assets/barshan-avatar.png",bio:"Hello",threadsTag:"barshaann",verified:!1,postsCount:3,followersCount:3000,followingCount:82,dashboardViews:947000,highlights:[{id:"hl1",name:"",image:"/assets/barshan-hl1.png"},{id:"hl2",name:"",image:"/assets/barshan-hl2.png"},{id:"hl3",name:"",image:"/assets/barshan-hl3.png"}],categories:[],dashboard:{views:947000,viewsTotal:947000,accountsReached:587140,followers:3000,reachByContent:{reels:72.4,posts:22.1,stories:5.5},sources:{explore:48.2,home:31.5,profile:12.8,other:7.5}}},posts:[{id:"p1",type:"image",image:"/assets/barshan-p1.png",caption:"",likes:1420,views:320000,comments:[{id:"c1",username:"alex",text:"Stunning colors!"}],shares:45,reposts:12,saves:89,date:"2 days ago",timestamp:Date.now()-172800000},{id:"p2",type:"image",image:"/assets/barshan-p2.png",caption:"Still life bouquet 💐",likes:2850,views:410000,comments:[{id:"c2",username:"nature_art",text:"Masterpiece"}],shares:92,reposts:34,saves:180,date:"5 days ago",timestamp:Date.now()-432000000},{id:"p3",type:"image",image:"/assets/barshan-p3.png",caption:"",likes:1980,views:217000,comments:[{id:"c3",username:"studio_lens",text:"Lighting on point"}],shares:60,reposts:18,saves:110,date:"1 week ago",timestamp:Date.now()-604800000}]}'''

start_qs = idx_js.find('qs={profile:{username:"deshdharm_news"')
end_qs = idx_js.find(';function Hj()', start_qs)

if start_qs != -1 and end_qs != -1:
    idx_js = idx_js[:start_qs] + barshaann_profile_code + idx_js[end_qs:]
    print("✓ Replaced default profile in index-NM4phaV4.js with @barshaann")
else:
    print("! Could not find qs bounds in index-NM4phaV4.js")

# Also in Hj(), if the stored profile in localStorage is deshdharm_news, ignore it and return qs:
idx_js = idx_js.replace(
    'return t.profile.dashboard',
    'if(t?.profile?.username==="deshdharm_news")return qs;return t.profile.dashboard'
)

with open(idx_path, 'w', encoding='utf-8') as f:
    f.write(idx_js)


# 4. Patch login.html
login_html_path = os.path.join(BASE_DIR, 'login.html')
with open(login_html_path, 'r', encoding='utf-8') as f:
    l_html = f.read()

redirect_script = '<script>try{localStorage.setItem("ig-access-activated","1");localStorage.setItem("ig-access-key","ACTIVE");window.location.replace("/app");}catch(e){window.location.replace("/app");}</script>'
if '<head>' in l_html and 'window.location.replace("/app")' not in l_html:
    l_html = l_html.replace('<head>', '<head>' + redirect_script)
    with open(login_html_path, 'w', encoding='utf-8') as f:
        f.write(l_html)
    print("✓ Added redirect script to login.html")


# 5. Patch app.html
app_html_path = os.path.join(BASE_DIR, 'app.html')
with open(app_html_path, 'r', encoding='utf-8') as f:
    a_html = f.read()

setup_script = '''<script>
try {
    localStorage.setItem("ig-access-activated", "1");
    localStorage.setItem("ig-access-key", "ACTIVE");
    // Clear legacy test profile if present so fresh barshaann profile displays
    var p = localStorage.getItem("ig-clone-v13");
    if (p && p.indexOf("deshdharm_news") !== -1) {
        localStorage.removeItem("ig-clone-v13");
    }
} catch(e) {}
</script>'''

if '<head>' in a_html and 'ig-access-activated' not in a_html:
    a_html = a_html.replace('<head>', '<head>' + setup_script)
    with open(app_html_path, 'w', encoding='utf-8') as f:
        f.write(a_html)
    print("✓ Added setup script to app.html")

print("Done patching.")
