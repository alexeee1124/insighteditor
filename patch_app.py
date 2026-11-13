import os

JS_FILE = "/Users/barshan/.gemini/antigravity/scratch/instastudio-app/assets/app-CWTZwhDb.js"

with open(JS_FILE, "r", encoding="utf-8") as f:
    content = f.read()

start_marker = "async function h(){const g=r.trim();if(g){i(!0);try{"
end_marker = "finally{i(!1)}}}"

idx1 = content.find(start_marker)
assert idx1 != -1, "start_marker not found"

idx2 = content.find(end_marker, idx1)
assert idx2 != -1, "end_marker not found"
idx2 += len(end_marker)

old_block = content[idx1:idx2]
print(f"Found old block of length {len(old_block)}")

new_block = """async function h(){
    const g = r.trim();
    if(g){
        i(!0);
        try {
            console.log("Cloning username:", g);
            const p = await d({ data: { username: g, ...Re() } });
            console.log("Clone server response:", p);
            if(!p || !p.ok){
                const errMsg = (p && p.error) || ("Could not import @" + g);
                V.error(errMsg);
                /api key|credit|token|configured|refused/i.test(errMsg) && f(!0);
                return;
            }
            const x = p.profile || p;
            const rawPosts = Array.isArray(x.posts) ? x.posts : [];
            const v = rawPosts.map((y, C) => {
                const N = Math.max(y.views || 0, y.likes || 0);
                const S = (y.likes || 0) + (y.commentsCount || 0);
                const P = I => +(I / Math.max(N, 1) * 100).toFixed(2);
                const O = Math.round(S * 0.07);
                const F = Math.round(S * 0.09);
                const X = Math.round(S * 0.03);
                const B = hu(y.id || `ig-${C}`);
                const H = y.durationSecs > 0 ? y.durationSecs : 0;
                const oe = H > 0 ? Math.max(2, Math.round(H * (0.3 + fe(B, 9) * 0.35))) : 8;
                const Q = (y.comments || []).slice(0, 3).map((I, E) => ({
                    id: `c-${C}-${E}`,
                    username: I.username || "user",
                    text: (I.text || "").slice(0, 200)
                }));
                const ee = +(10 + fe(B, 8) * 35).toFixed(1);
                return {
                    id: y.id || `ig-${C}`,
                    type: y.type || "reel",
                    image: y.image || "",
                    caption: y.caption || "",
                    likes: y.likes || 0,
                    comments: Q.length ? Q : [{ id: `c-${C}`, username: x.username || "creator", text: (y.caption || "").slice(0, 60) || "🔥" }],
                    shares: O,
                    reposts: X,
                    saves: F,
                    date: Or(y.timestamp),
                    views: N,
                    accountsReached: Math.round(N * 0.62),
                    followersPct: ee,
                    watchTime: fu(Math.round(N * 8)),
                    avgWatchTime: Ir(oe),
                    interactions: S,
                    profileActivity: Math.round(N * 0.012),
                    profileVisits: Math.round(N * 0.01),
                    follows: Math.round(N * 0.002),
                    initialPlays: Math.round(N * 1.08),
                    replays: Math.round(N * 0.16),
                    retention: mu(B),
                    duration: H > 0 ? Ir(H) : "0:32",
                    publishedAt: `${Or(y.timestamp)} at ${uu(y.timestamp)}`,
                    skipRate: +(2.4 + fe(B, 11) * 4).toFixed(1),
                    shareRate: P(O),
                    likeRate: P(y.likes || 0),
                    saveRate: P(F),
                    repostRate: P(X),
                    commentRate: P(y.commentsCount || 0),
                    srcReelsTab: y.type === "reel" ? +(45 + fe(B, 5) * 40).toFixed(1) : +(8 + fe(B, 5) * 14).toFixed(1),
                    srcExplore: +(3 + fe(B, 6) * 9).toFixed(1),
                    srcProfile: +(2 + fe(B, 7) * 8).toFixed(1),
                    engagementCurve: pu(B),
                    audFollowersPct: ee,
                    audAge: [
                        { label: "13-17", pct: 9.1 },
                        { label: "18-24", pct: 35.2 },
                        { label: "25-34", pct: 35.6 },
                        { label: "35-44", pct: 12.6 },
                        { label: "45-54", pct: 4.5 },
                        { label: "55-64", pct: 1.5 },
                        { label: "65+", pct: 1.4 }
                    ],
                    audCountry: [
                        { name: "India", pct: 86.4 },
                        { name: "United States", pct: 4.2 },
                        { name: "Pakistan", pct: 2.1 },
                        { name: "Bangladesh", pct: 1.8 },
                        { name: "Nepal", pct: 1.1 }
                    ],
                    audGender: { women: 46.2, men: 53.8 }
                };
            });
            const b = v.reduce((y, C) => y + (C.views || 0), 0);
            const w = v.reduce((y, C) => y + (C.interactions || 0), 0);
            const k = v.filter(y => y.type === "reel").reduce((y, C) => y + (C.views || 0), 0);
            const j = Math.max(0, b - k);
            const rawExtUrl = typeof x.externalUrl === "string" ? x.externalUrl : "";
            const cleanThreadsTag = rawExtUrl ? rawExtUrl.replace(/^https?:\\/\\//, "").replace(/\\/$/, "") : "";
            n(y => {
                const curProf = (y && y.profile) || {};
                const curDash = curProf.dashboard || {};
                return {
                    ...y,
                    profile: {
                        ...curProf,
                        username: x.username,
                        displayName: x.displayName || x.username,
                        avatar: x.avatar || curProf.avatar,
                        bio: x.bio || "",
                        threadsTag: cleanThreadsTag,
                        verified: Boolean(x.verified),
                        postsCount: x.postsCount || v.length,
                        followersCount: x.followersCount || 0,
                        followingCount: x.followingCount || 0,
                        dashboardViews: b,
                        dashboard: {
                            ...curDash,
                            views: b,
                            viewsTotal: b,
                            accountsReached: Math.round(b * 0.62),
                            followers: x.followersCount || curDash.followers || 0,
                            reachByContent: {
                                ...(curDash.reachByContent || {}),
                                reels: k,
                                posts: j
                            },
                            interactionsByContent: {
                                ...(curDash.interactionsByContent || {}),
                                reels: Math.round(w * (k / Math.max(b, 1))),
                                posts: Math.round(w * (j / Math.max(b, 1)))
                            },
                            contentShared: {
                                ...(curDash.contentShared || {}),
                                reels: v.filter(C => C.type === "reel").length,
                                posts: v.filter(C => C.type === "post" || C.type === "image").length
                            },
                            profileVisits: Math.round(b * 0.02)
                        }
                    },
                    posts: v.length > 0 ? v : ((y && y.posts) || [])
                };
            });
            V.success(`@${x.username} imported — ${v.length} posts`);
            t(!1);
        } catch (err) {
            console.error("Clone account error:", err);
            V.error("Import failed: " + (err && err.message || err));
        } finally {
            i(!1);
        }
    }
}""".strip()

new_content = content[:idx1] + new_block + content[idx2:]

with open(JS_FILE, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Successfully replaced function h in app-CWTZwhDb.js!")
