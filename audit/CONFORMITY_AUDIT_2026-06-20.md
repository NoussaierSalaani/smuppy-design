# Conformity Audit vs RN app — 2026-06-20

100 screens audited, 23 conform. 64 P0 / 150 P1 / 241 P2.

## P0 (must fix)

### Signup
- [missing] Name field (Nom / 'Ton nom', person glyph) absent in Figma. RN truth + maquette JSDoc + fixtures require Name -> Email -> Password; Figma jumps title -> Email -> Password.

### Nouveau mot de passe
- [icon] Lead icon circle shows a magnifying-glass/search glyph; RN screen is a password screen (lead circle = key/🔑 fallback, fields = lock). Wrong glyph for new-password.

### TellUs
- [missing] Username field (required, with live availability status dot + helper/error) is a core RN section but absent from the Figma frame.

### BusinessInfo
- [missing] Category section absent in Figma: RN has categoryTitle 'Type d’activité' + 6 single-select chips (gym/yoga/crossfit/boxing/pilates/wellness). Core controlled-form section entirely missing from the maquette.

### PeaksFeed
- [missing] Figma renders the wrong screen entirely: a Fan/Vibes/Xplorer Home/Discover feed (Peaks&Live carousel + 'Suggestions pour toi' fan cards + 'Ta tribu' post feed). RN PeaksFeed is a Peaks/Live 2-tab segmented grid. None of the RN structure (segmented tabs, chip row, 2-col PeakLiveCard grid) is present.
- [header] Header mismatch: Figma shows Smuppy logo + bell(badge 3) + search icon. RN PeaksFeed header = BackButton (‹) + centered [Peaks][Live] segmented pill tabs only — no logo, no bell, no search.

### Search
- [nav] Figma shows a bottom nav (home/play/+/circle/avatar) AND a header back-chevron simultaneously. RN SearchView is a back-button sub-screen with NO bottom nav — dual-nav is contradictory; render should have back-only, not bottom nav.

### PostComposeDetailsView
- [missing] WRONG SCREEN: Figma 245:1693 renders an activity Run-recap ('Run du matin 🏆', map route, KM/TEMPS/CAL stat tiles, 'Splits par km' bars, 'Repartager ce run' CTA), NOT the RN PostComposeDetailsView (post compose: 'Nouveau post', caption, audience, hashtags, Publier). The two screens are unrelated — frame ID maps to a different view.
- [missing] Entire RN structure absent from Figma: media-preview tile + multiline caption + char counter, 'Qui peut voir ?' audience radios (Public/Mes fans/Privé), 'Ajouter un lieu' location row, 'Hashtags' chips — none present in the rendered frame.

### PostDetailView
- [missing] SCREEN MISMATCH: Figma 245:1776 renders the Create-Post composer ('Nouveau post' / 'Écris une légende…' / 'Publier'), which maps to RN AddPostDetailsScreen + PostComposeDetailsView — NOT PostDetailView. PostDetailView is a display-only over-media post viewer; none of its sections appear in the Figma frame.
- [header] Figma has a light solid header bar with centered title 'Nouveau post' + back chevron + mint 'Publier' pill. PostDetailView has NO header title and NO publish CTA — it uses over-media chrome (transparent back '‹' + menu '⋯' on a dark scrim).
- [cta] Figma shows a filled mint-gradient 'Publier' pill (top-right). PostDetailView has no submit/publish CTA at all; its only CTA is the outlined 'Fan' become-a-fan button (borderWidth 1.5, radius 22, no fill).
- [missing] PostDetailView core elements all absent from Figma: author row+avatar, caption display, location/tagged meta rows, and the right-rail share/like/save action glyphs (➤ ♡ ☆) + likes-count pill. Figma instead shows hashtag chips, location/fans/visibility list rows, and 'Paramètres avancés'.

### ActivityLeaderboardView
- [missing] Sort segmented tabs (Plus rapide / Distance / Meilleur rythme) are entirely absent from the Figma frame — RN has a mandatory tablist driving fastest_time/longest_distance/best_pace sort. Core interaction missing.
- [icon] Figma uses trophy/medal/person glyph icon-tiles in the rank slot; RN renders the rank DIGIT (1/2/3) inside a medal chip (and plain digit otherwise). Wrong rank representation — glyphs replace the numeric rank.

### CoachJournalView
- [missing] Figma shows a session-NOTES log; RN is a participant ROSTER. Entire row model diverges: RN rows = Avatar + @username + sessions-count + star rating + 'rated N' badge. Figma rows = mint edit-icon + session name + date·note + chevron. No avatars/usernames at all in Figma.
- [missing] RN rating stat is core (★ stars graphic + 'rated N' badge per row). Figma has NO rating stars and NO rated badge — the entire rating/scoring surface is absent.

### PrescriptionsView
- [text] Header title mismatch: Figma 'Prescriptions' (+ eyebrow 'MON SUIVI', H1 'Prescriptions', subtitle 'Plans actifs de ton coach') vs RN 'Missions bien-être'. Entire screen concept diverges (coaching PLANS list vs wellness MISSIONS list).
- [missing] RN renders separate bordered cards w/ description + 'Commencer' Button + difficulty dots + category word + weather badge. Figma has NONE of these: single white container, rows w/ status pill ('Actif'/'Fini'), meta '3x/semaine - 4 semaines', no description/CTA/dots/category/weather.

### RunCountdownView
- [missing] Cancel button absent: RN renders an 'Annuler' pill near bottom (styles.cancel, cancelLabel prop); Figma frame has no cancel affordance — primary interactive element missing.

### PrescriptionPreferencesView
- [missing] Figma omits all 3 single-select option groups (Niveau d'activite low/medium/high, Activites en exterieur, Frequence) that are core to RN. Only a single toggle card is shown.
- [cta] No Save CTA. RN has a mint solid Button 'Enregistrer' (double-submit guarded). Figma frame has no save button at all.
- [text] Strings mismatch: Figma rows are notification-style (Rappels de seance / Plan hebdomadaire / Conseils du coach / Suivi nutrition). RN categories are Mouvement / Pleine conscience / Social / Creativite / Nutrition. Title is 'Mes prescriptions' vs RN 'Preferences de missions'.

### RunHistoryView
- [nav] Figma shows a bottom tab-bar (home/peaks/+/chat/profile) but RunHistoryView is a sub-screen with a back button — back-button screens must NOT render the bottom-nav. Conflicting nav affordance.

### RunTrackingView
- [missing] Figma frame 245:2703 renders as an EMPTY pale-mint grid placeholder — none of the RN screen content exists. Frame is blank/unbuilt, not a real RunTracking layout.
- [missing] No metric stats card: RN hero distance StatTile (5,2 km) + Duree/Allure/Cadence/Calories grid are entirely absent from the Figma frame.
- [missing] No pause/resume + STOP (Terminer) control buttons present in Figma; RN has two control pills (~52px, radius 16, danger STOP).

### SpotDetailView
- [missing] Figma frame 245:2765 is a Run/Activity summary ('Run du matin 🏆', stats grid + 'Splits par km' + 'Repartager ce run') — NOT the spot detail. Wrong frame mapped to SpotDetailView; the whole comparison surface is mismatched.
- [missing] All RN spot sections absent from Figma: rating summary '4,5 (42 avis)' + stars, category chip 'Course à pied', 'Suggéré par {creator}' row, qualities chips ('Atouts'), and the reviews FlatList ('Avis').

### ChannelDetailView
- [missing] Figma node 245:2895 renders a Run-recap screen (route map, stat tiles KM/TEMPS/pace/CAL, 'Splits par km' pace bars), NOT the channel detail. Entire RN structure (hero cover, channel name/tagline Card, ACCÈS PREMIUM price pill, perk check rows) is absent.
- [missing] RN core sections all missing in Figma: overlapping elevated Card with channelName+tagline, 'ACCÈS PREMIUM' premium pill with $9.99 / mois price, and 'Inclus dans l'abonnement' perk check-row list.
- [cta] CTA text mismatch: Figma shows 'Repartager ce run'; RN ChannelDetailView CTA is 'S’abonner · $9.99/mois' (subscribe, money guard) or 'Gérer mon abonnement' when subscribed. (Gradient style/size ~54h ~28r is otherwise correct.)

### KycCompanyView
- [missing] Figma is a FORM with 4 editable input fields (Raison sociale, Numéro d'enregistrement, Pays, Adresse du siège) each with a value; RN renders read-only ListRow steps (registration#, legal rep, beneficiaries, bank account) with NO input fields. Entire data-entry surface absent in RN.

### ManageSubscriptionView
- [missing] Figma frame 245:3119 renders ONLY the header (786x330px) — entire body is blank. All RN content is absent: compliance Banner, 'Abonnement Smuppy' section + platform card, 'Abonnements aux créateurs' channel cards, 'Gérer' rows, footer legal.

### MySubscriptionsView
- [cta] Figma adds a bottom full-width mint-gradient CTA 'Gerer les abonnements' that does NOT exist in RN. RN manages each sub via per-card Voir/Annuler/Reactiver Buttons; no global bottom CTA.
- [missing] RN per-card action buttons (Voir / Annuler / Reactiver) and the cancel/reactivate flow are entirely absent from the Figma frame, which only shows a passive 'Actif' status pill.

### PackageDetailView
- [missing] Frame 245:3223 renders a Run/activity recap screen ('Run du matin', map route, KM/TEMPS/PK/CAL stat tiles, 'Splits par km', 'Repartager ce run'), NOT the PackageDetailView creator-pack purchase screen. Whole screen mismatch — wrong frame ID mapped to this component.
- [missing] RN core sections absent from Figma render: no hero cover with BEST SELLER/MEILLEURE VENTE badge, no pack title+tagline ('Transformation · 3 mois' / 'Coaching par Sara Khan'), no price block (priceLabel/oldPriceLabel struck/savings pill), no 'Ce qui est inclus' ListRow perks.
- [cta] RN CTA is buy/access ('Acheter le pack · $269' or 'Réserver une session', gradient lg Button). Figma CTA reads 'Repartager ce run' (re-share run). Wrong label and wrong purpose entirely.
- [text] All header/strings diverge: RN headerTitle='Pack' vs Figma 'Run du matin 🏆'. No matching strings between rendered frame and RN truth.

### PlatformSubscriptionView
- [missing] Figma shows a SIDE-BY-SIDE two-plan picker (Pro Creator 99$ + Pro Business 49$). RN is an account-type MANAGEMENT view with ONE active plan card and explicitly 'never a side-by-side picker' (PlatformSubscriptionScreen mirror). Wrong layout/intent.
- [text] Unlock list content fully diverges. Figma: Posts & peaks illimites / Aucune publicite / Badge verifie / Themes premium / Telechargement HD / Support prioritaire. RN truth: Aller en live / Abonnements de chaine / Recevoir des Smups / Sessions 1:1 / Events / Cours VOD. None match.

### ChannelOwnerView
- [cta] Figma footer = single OUTLINE button 'Voir l'analytique'. RN truth = TWO buttons: primary gradient 'Gérer la chaîne' + outline 'Modifier'. Wrong count + wrong labels.

### NotificationsView
- [missing] Figma frame 245:3802 renders the Notification SETTINGS screen (toggle list 'Choisis quelles notifications recevoir', sections ENGAGEMENT/SESSIONS & RAPPELS/PAIEMENTS), NOT the activity inbox that NotificationsView implements. Whole screen identity mismatch — it maps to NotificationSettingsView, not NotificationsView.
- [missing] None of NotificationsView's core elements appear: no actor rows (avatar+name+message+time), no follow/follow-back CTA, no new-dot unread indicator, no Aujourd'hui/Plus tôt section grouping.

### SecuritySettingsView
- [missing] Figma frame body is entirely blank — the MFA/2FA status hero banner (shield + Activée/Désactivée + Activer CTA) present in RN is absent.
- [missing] All three RN card sections (Authentification, Mot de passe, Sessions actives) and their rows are missing from the Figma frame.

### BlockedRegionView
- [missing] Figma omits the entire action stack: RN has Notify-me primary CTA ('Préviens-moi quand c'est disponible'), Learn-more outline CTA, and Sign-out link. Figma shows only a single 'Retour à l'accueil' button — none of the 3 canonical CTAs are present.

### EditInterestsView
- [header] Figma renders the ONBOARDING variant (back + progress bar '2/3'), not the settings header. RN EditInterestsView has back + centered title 'Centres d'intérêt' + trailing Save button. Header grammar fully diverges.
- [cta] RN EditInterestsView saves via a header Save button gated by hasChanges/isSaving. Figma has NO Save button and instead a full-width bottom 'Continuer' CTA — wrong save model for the settings screen.

### FansListView
- [text] Trailing CTA label wrong: Figma shows 'Fan' (solid) + 'Devenir fan' (outline). RN truth = 'Suivre' (track/follow-back gradient Button) or a ⇄ mutual indicator. Labels and follow-back semantics don't match.

### MatchPageView
- [missing] Figma renders only a 'Composition / 11 joueurs · 3 remplaçants' summary card; RN's Man-of-the-Match card, Photos strip, and 'Meilleures notes' (top abilities) sections are entirely absent from the Figma frame.

### PlayerCareerCardView
- [missing] Figma adds a secondary link 'Télécharger en PNG' under the Share CTA. RN has only ONE share button (onShare); no download/PNG-export action or label exists in the component or props.

### EditExpertiseView
- [cta] Figma shows a bottom full-width mint-gradient 'Continuer' CTA. RN EditExpertiseView has NO bottom button — this is the Onboarding sibling's pattern. Settings screen saves via an inline header Save, doc states 'NO Continue/Skip'.
- [missing] RN header has an inline Save button ('Enregistrer', gated by hasChanges/isSaving) at top-right. Figma header has only the back chevron — the Save control is absent.

### GoLiveIntroView
- [missing] Wrong screen: Figma 245:4600 renders the GoLiveView live-config screen (TITRE DU LIVE field, ACCÈS tiers, PRÉVISUALISATION), not GoLiveIntroView. Entire intro surface absent.
- [missing] Hero card missing: no videocam icon chip, no heroTitle 'Anime ton premier live' / heroSubtitle, no red 'EN DIRECT' LIVE badge over scrim.

### GoLiveView
- [cta] Primary 'Démarrer le live' gradient mint CTA (Button variant=gradient, pill radius, monetisation gate) is MISSING from the Figma frame — RN always renders it as a bottom CTA bar.

### LiveEndedView
- [missing] Figma adds a 5-star rating block ('TU AS KIFFÉ CE LIVE ?' + 5 stars) that RN deliberately OMITS — contract states NO star rating (this is a creator recap, not rate-your-session). Forbidden surface.
- [cta] Gradient CTA label mismatch: Figma '👊 Envoyer des Smups à Sara' (viewer/fan action) vs RN 'Voir les revenus' (creator money CTA). Wrong action + wrong audience.
- [cta] Outline CTA label mismatch: Figma \"S'abonner à la chaîne\" vs RN 'Partager le replay'. Subscribe doesn't belong on creator's own ended-live recap.

### BusinessDiscoveryView
- [dimension] Card layout mismatch: Figma cards are horizontal (small ~90px square cover swatch on LEFT, text to the RIGHT). RN renders a full-width cover Image on TOP (width 100%, height 160) with text stacked BELOW. Fundamentally different card structure.

### DisputeCenterView
- [cta] Figma create CTA = full-width BOTTOM gradient button '+ Ouvrir un litige' (mint→teal/blue gradient). RN renders create as a small 'Nouveau' Button atom in the HEADER (solid mint). Wrong position AND wrong style/label.
- [icon] Figma shows status ICON tiles per row (orange clock for open, green check-circle for resolved) in rounded colored squares. RN has NO icons — status is an 8px decorative dot only. Missing icon glyphs.

## P1

### AccountType
- [missing] Figma uses stale legacy 2-step grouping (Personnel + intermediate 'Professionnel' card + 'QUEL TYPE DE PROFESSIONNEL ?' disclosure). RN truth flattens to 3 canonical cards (personal/pro_creator/pro_business) in one tap — extra Professionnel card + disclosure header do not exist in RN.
- [cta] No 'Continue' CTA in Figma. RN has a sticky gradient lg Button 'Continuer' (footer, disabled until selection). Missing CTA + missing gating affordance in Figma.
- [icon] Right affordance mismatch: Figma shows chevron '>' on every card. RN renders an unselected radio ring / selected mint check-dot (✓) instead — selection model differs (tap-navigate vs controlled radio + Continue).

### Nouveau mot de passe
- [color] Strength label 'Mot de passe fort' rendered in literal mint #0EBF8A (~2.38:1 on light surface = WCAG AA fail). RN overrides to AA-safe primary token (guarded by regression test); Figma deviates.

### TellUs
- [text] Subtitle mismatch: Figma 'Aide-nous a personnaliser ton experience' vs RN i18n 'Cree ton profil pour que les gens puissent te reconnaitre'.

### Interests
- [emoji] Figma chips use emoji glyphs (⚽🏀🎾💧🏃🚴 etc.) for both chip icons and section tiles. RN truth renders vector Ionicons (config/interests.ts: 'football','water','walk'…) tinted with the category hue (V1 <Ionicons size=16>, V2 icon node). Emoji = wrong glyph system, untinted, no hue match.
- [icon] Section-header tiles in Figma show emoji (⚽ Sports, 🐕 Fitness) instead of the hue-tinted Ionicons glyph the RN section icon expects (V1 section.icon via <Ionicons size=18 color=section.color>; V2 sectionIcon tile renders cat.icon node).

### Profession
- [missing] Figma is a MULTI-select categorized grid (2 chips selected at once: 'General Fitness' + 'Vinyasa Flow' both mint-outlined). RN OnboardingProfessionView is single-select (one selectedId across all sections). Documented as intentional in header comment, but is a real structural divergence from the maquette.

### Expertise
- [icon] Chip glyphs are placeholder/wrong: heart on 'Boxing', 'Muay Thai', 'Stress Management' and a sun on 'Mindfulness' — non-semantic icons that do not represent the expertise. RN passes icons via props; maquette wired generic placeholders instead of category-correct glyphs.

### MfaBackupCodes
- [text] Banner copy differs: Figma = 'Sauvegarde-les maintenant. Tu ne pourras plus les revoir. Chaque code n'est utilisable qu'une fois.' vs RN warningMessage 'Chaque code ne fonctionne qu'une fois. Ils te permettent de te connecter si tu perds ton téléphone.'

### BusinessInfo
- [missing] Website (optional) Input missing in Figma. RN renders a 3rd field 'Site web (optionnel)' with url keyboard between Adresse and the info note.
- [text] Title/subtitle/info-note copy diverge: Figma 'Détails de l\\'entreprise' / 'Parle-nous de ton entreprise' / '...logo, téléphone, site web... dans les Réglages' vs RN 'Ton activité' / 'Présente ton établissement aux Smuppers' / 'Tu pourras compléter ton profil plus tard.'
- [color] Logo caption 'Ajouter ton logo' rendered in raw bright mint (~#22C58E, AA-fail ~3.2:1 on light) in Figma. RN swaps to adaptive theme.primary (light #176A5A) for AA. Same mint-text-on-light trap.

### BusinessCategory
- [text] Title/subtitle mismatch: Figma 'Catégorie d'activité' + 'Choisis le type d'activité qui décrit le mieux ton entreprise'; RN i18n = 'Type d'activité' + 'Quel type d'activité as-tu ?'.
- [missing] Figma has an 'AUTRE CATÉGORIE' section with a free-text input ('Écris ta catégorie'). RN view has NO custom/other-category text input prop or section — entirely absent.

### Guidelines
- [icon] Figma item rows use green filled check-square glyphs as leading icon; RN ListRow uses a hue-colored bullet '•' fallback. Glyph mismatch per guideline item.
- [text] Item strings differ. Figma: 'Sports et bien-être – Fitness, nutrition, relaxation...', 'Science du sport et innovation santé...'. RN canonical: 'Respecte les autres membres de la communauté', 'Partage du contenu positif et constructif'.
- [missing] RN has a sticky accept-checkbox row ('J'ai lu et j'accepte les règles...') above the CTA gating Continue; Figma render shows only the CTA, no accept checkbox visible.

### HomeFeed
- [header] Topbar icon order flipped: Figma shows bell+red-badge on LEFT and search on RIGHT; RN canonical (HomeFeedView L1474-1518) is search LEFT, wordmark CENTER, bell+badge RIGHT.

### FanFeed
- [color] Section headings ('Peaks & Live', 'Suggestions pour toi', 'Ta tribu') render BLACK/dark in Figma, but RN HomeFeedView (SectionHeading, line 1140-1145) renders them in canonical BRAND_MINT #26C1A4. Mint heading color is the founder-locked canonical, Figma is non-conform.
- [text] Suggestion CTA reads 'Devenir fan' in Figma, but RN canonical becomeFanLabel = 'Fan' (HomeFeedView DEFAULT_LABELS line 432 + v2HomeFeedView.json). Real app shows a shorter 'Fan' chip, not 'Devenir fan'.

### VibesFeed
- [header] Topbar icons inverted: Figma places the notification bell on the LEFT and search on the RIGHT. RN spec/HomeFeedView shell is search LEFT, notifications RIGHT. Mirrored layout.
- [text] Image-card author chips show @-handles ('@alex_vibes', '@sara_k'). RN contract: author is a DISPLAY name only, never a @username/handle (props doc + fixtures use 'Alex Rivera'/'Sara Kovac'). Violates handle rule.

### PeaksFeed
- [nav] Top tabs wrong: Figma = Fan/Vibes/Xplorer (3 tabs). RN PeaksFeed = 2-segment [Peaks][Live] pill-card TabBar. Also RN has a category chip row (Tous/Challenge/Following/Trending) absent from Figma.
- [missing] RN 2-column virtualized PeakLiveCard grid (peak ▶views pill / live 👁viewers pill + red LIVE badge, cards ~48.5% width, radius from PeakLiveCard) is entirely absent from the Figma frame.

### Search
- [missing] 'Lieux près de toi' (places) section absent from Figma render. RN SearchView renders 4 sections (Tendances, En direct, Créateurs suggérés, Lieux près de toi); Figma shows only the first 3.

### Notifications
- [icon] Corner type-badges render as hollow colored RINGS with no glyph inside. RN truth (NOTIFICATION_ICON_MAP) draws a white Ionicons glyph inside the colored badge: like=heart/pink, follow=person-add/green, live=radio/red, payment=card/green, message=chatbubbles/blue. Figma badges are empty.
- [missing] Dark rounded rectangle placeholder sits on row 1 (Emma Chen) where a post thumbnail / control belongs — unresolved black placeholder asset, not in RN truth.

### ChatView
- [color] Sent bubbles in Figma use a mint→deep-teal GRADIENT fill; RN renders a FLAT solid #176A5A (SENT_BUBBLE_BG, no gradient). Bubble visual style diverges.
- [missing] Figma shows a rich shared-POST link-preview card (pin icon + 'Post de Sara Khan' + 'Sunrise yoga · Mont-Royal' + time). RN only supports a plain 200x200 image bubble (mediaUri); no shared-post/link-preview card structure exists.

### NewMessage
- [missing] RN rows render a second-line @username handle (handle style, onSurfaceVariant) under each name; Figma rows show name only — username subtitle missing on every recipient row.
- [missing] RN renders a trailing chat glyph (chatIcon / chatDot) on the right of every recipient row; Figma rows have no trailing icon.

### CreateGroupChatView
- [icon] Photo placeholder icon: Figma shows a mint concentric-ring/target glyph; RN renders a 📷 camera emoji default (cameraIcon='📷'). Glyph mismatch.
- [missing] Selected-member chips: RN renders avatar (32px) + name + removable '×' glyph per chip; Figma chips show name-only, NO avatar, NO remove × — chip structure incomplete in design.

### PostComposeDetailsView
- [cta] Figma CTA text is 'Repartager ce run'; RN CTA label is 'Publier'. Text/intent mismatch (though both use a mint gradient pill with radius ~28, height looks ~54 — gradient style itself is consistent with RN Button variant='gradient' size='lg').
- [header] Figma header = circular X close (left) + 'Run du matin 🏆' title + share glyph (right). RN header = BackButton '‹' + centered title + balancing spacer (no share icon, no X-close). Header pattern diverges.

### PostDetailView
- [color] Figma is a light adaptive surface (#F2F4F4-ish bg, white cards, dark text). PostDetailView happy-path is a CONSTANT dark base (#000 scrim) with white over-media ink — opposite surface model; cannot be light/dark compared as the same screen.
- [icon] Figma uses colored gradient/solid square thumbnails (blue/purple/mint) as list-row leading icons + chevrons; PostDetailView uses text-glyph icons over media (back ‹, menu ⋯, share ➤, heart ♥/♡ in LIKE_RED, bookmark ★/☆ in SAVE_MINT). No glyph overlap between the two surfaces.

### PostLikersView
- [text] Follow CTA label mismatch: Figma reads 'Devenir fan'; RN renders 'Suivre en retour' (follow-back) / 'Abonné·e' (already-following). Wrong string + wrong semantics.
- [missing] Figma rows omit the username secondary line (@handle); RN always renders username under the name via rowMeta. All 6 rows missing it.

### PostGalleryView
- [cta] 'Suivant' CTA: RN uses Button variant='solid' (filled mint background, t.colors.primary) but Figma renders an outline-only mint pill (transparent fill + mint border + mint text). Style mismatch — should be solid mint when a media is selected/enabled.
- [nav] Camera entry placement: RN renders the camera tile as the FlatList ListHeaderComponent (first grid cell). Figma instead shows a camera button on the RIGHT of the meta row ('Récents' row) and has NO camera tile in the grid. Structural divergence in camera affordance location.

### PeakCameraView
- [missing] RN canonical speed strip (Lent/Normal/1x/Rapide/Très rapide, selectable, above duration chips) is absent from the Figma frame — only duration chips render.

### HashtagFeedView
- [dimension] Play badge: Figma renders a large ~56px white circle with a black play triangle (top-left); RN playWrap slot is only 16x16 with a tiny 12px playDot and no white circle backing. Badge oversized + missing circular surface in Figma vs RN.

### ActivityLeaderboardView
- [color] Rank pills in Figma are amber/grey (Toi '+0:33' on amber #F5C…, '2e'/'3e' grey, only '1er' mint). RN medal palette is gold/silver/bronze (#B45309/#475569/#92400E light) and the current-user badge is mint 'primary', never amber. Off-palette amber pill.
- [missing] RN avatar slot (Avatar image OR initials fallback) is missing — Figma shows generic mint icon tiles instead of participant avatars, so per-user identity is lost.

### BusinessBookingView
- [dimension] Step indicator: RN renders dot-on-top + label-below (square-ish stepDot radius 10, 30x30). Figma renders horizontal rounded PILLS (number-circle + label side-by-side). Layout mismatch.
- [color] Selected day (MAR 4) is OUTLINE-only in Figma (white bg, mint border + mint text). RN fills selected day with primary bg + onPrimary text. Selection state style diverges.
- [color] Selected slot (10:00) is OUTLINE-only in Figma (white bg, mint border, mint text). RN fills selected slot with primary bg + onPrimary text. Same divergence as date strip.

### CoachJournalView
- [missing] RN has a count header ('42 participants') under the title. Figma replaces it with a 'COACHING' eyebrow label + subtitle 'Notes de séances' — the participant count header is missing.
- [icon] Figma uses a trailing chevron '>' on each row; RN row has NO chevron (whole row is Pressable, trailing slot is the rating stars). Also Figma leading icon = mint edit-pencil square, RN leading = circular Avatar (photo/initials).
- [text] Title mismatch: RN title 'Carnet du coach' / subtitle is activity name ('Yoga du matin'); Figma title 'Journal du coach' / subtitle 'Notes de séances'. Back-button label text 'Journal' (Figma) not in RN (RN back is icon-only with a11y 'Retour').

### MySessionsView
- [missing] Figma adds a per-row 'Rejoindre' CTA button on the session row; RN MySessionsView has NO row CTA — rows are a plain Pressable with only a '›' chevron. Extra control absent from real component.
- [missing] Figma shows a 'PASSÉES (EXTRAIT)' section with a past row rendered below the upcoming card (both tabs at once). RN shows ONLY the active tab's list (one TabBar selection) and has no such section header — structural mismatch.
- [missing] Figma past row shows a '★★★★☆ noté' star rating. RN row has no rating element at all (avatar + name + title + status dot/meta + chevron only).

### PrescriptionsView
- [missing] Figma eyebrow 'MON SUIVI' + large display H1 + subtitle block is absent in RN (RN has only a single centered small header title, no eyebrow/subtitle/display-title).
- [cta] Figma per-row affordance = mint status PILL ('Actif' filled mint, 'Fini' grey). RN per-row = solid mint 'Commencer' Button or plain 'Terminé' text word. No status pill exists in RN.
- [missing] Figma rows show a mint rounded-square ICON tile (bar / arrow / plus glyph) per row. RN category icon is an optional caller-supplied slot (no default), and RN card layout is full bordered card, not an icon-tile row inside one container.

### RunCountdownView
- [color] Scrim too light: RN dims map with rgba(0,0,0,0.55) strong dark scrim; Figma shows near-undimmed light-grey map, reducing count contrast vs RN intent.

### PrescriptionPreferencesView
- [missing] Category count wrong: RN has 5 toggle rows incl. 'Social' and 'Creativite'; Figma shows only 4 and drops those two.
- [icon] Icon set diverges: Figma uses tinted-square line icons (bell/calendar/lightbulb/apple). RN category leadingIcon glyphs are emoji (run/yoga/handshake/palette/salad) with adaptive primary/onSurfaceVariant tint.

### RunHistoryView
- [missing] Figma run rows have a large dark-navy rounded thumbnail with a green line-chart glyph; RN ListRow is called with title+subtitle only (no leadingIcon/leadingTint) — that thumbnail does not exist in the RN component.
- [dimension] Figma renders 3 separate floating white cards per run; RN groups all rows in ONE bordered container (styles.list radius 20, hairline border). Card grouping/shape mismatch.
- [text] PR badge placement: Figma draws '🏆 PR' inside the subtitle line, overlapping the pace ('5'29\"/km') with a teal highlight artifact; RN appends '🏆 PR' to the row TITLE (e.g. '5,2 km  🏆 PR'), not the subtitle.

### RunRecordsView
- [missing] Summary StatTile grid ('Tes meilleures perfs' — best 5k/10k/longest/pace) is absent in Figma; RN renders it above the list when summary present.
- [dimension] Records shown as separate detached cards (gap per row) in Figma; RN renders all ListRows inside ONE outlined Card.
- [cta] Active 'Records' tab drawn as outline/stroke only (mint border, no fill). RN active tab uses Button variant='solid' = mint fill.

### RunStartView
- [missing] Bottom option toggles (Coach vocal / Écran allumé) present in RN (toggles row) are ABSENT from the Figma frame.
- [color] Figma bg is a LIGHT mint-green grid; RN root is #000 dark map with constant white inks (overlay designed for dark map both themes). Light/dark mismatch.

### RunTrackingView
- [missing] No live map slot + dark scrim background. RN root bg is #000 with map behind scrim; Figma shows only a flat mint #E2EAE6-ish grid.
- [missing] No GPS signal pill (Signal bon/faible/perdu) with colored dot+border, nor the weak/lost GPS Banner alert.

### ActivityAttendeesView
- [cta] Role badges: Figma uses FILLED pills (mint-fill 'Hote', amber-fill 'Attente'); RN renders OUTLINE-only badges (transparent fill, border+ink, radius 12). Fill style + visual weight mismatch.
- [missing] Figma count header has eyebrow 'PARTICIPANTS' (mint uppercase) + large 'Inscrits' title above the count line; RN renders only one countText line ('{{count}} participants'). Two header elements absent in RN.
- [dimension] Figma groups rows inside one rounded white CARD (radius ~20, elevated) with inset dividers; RN renders flat rows on surface bg with hairline bottom borders, no card container/radius/elevation.

### SpotDetailView
- [missing] RN route stats card has 2 cells (Distance, Temps estimé) + a difficulty meaning-pill ('Modéré'). Figma shows a 4-stat grid (KM/TEMPS//KM/CAL) with no difficulty pill — stat set and difficulty graphic missing.
- [cta] RN bottom bar = two side-by-side Buttons (outline 'Donner un avis' + gradient 'Itinéraire'). Figma shows a single full-width gradient CTA 'Repartager ce run' — wrong CTA labels, count, and layout vs RN.

### ActivityDetailView
- [missing] Stats card renders only 2 cells (Date, Lieu). RN STATS has 4: the accent Distance (5,2 km) and Participants (12/20) cells are absent in the Figma frame.
- [dimension] Cover/map hero is a thin placeholder bar ('Carte du parcours') instead of the RN 200px-tall rounded hero (styles.hero height:200, radius 20).

### ChannelDetailView
- [header] Header divergence: Figma uses a circular close (X) button left + share/expand arrow icon top-right + title 'Run du matin 🏆'. RN uses a plain BackButton (chevron) left, centered title='Sara's Channel', and NO right-side action icon.
- [nav] Both omit bottom-nav (correct for a sub-screen), but the left control differs: RN BackButton chevron vs Figma circular X close button — inconsistent dismissal affordance for this sub-screen.
- [text] All strings differ: Figma title 'Run du matin', stat labels KM/TEMPS/KM/CAL, 'Splits par km'. RN strings are channelName 'Sara's Channel', 'ACCÈS PREMIUM', 'Inclus dans l'abonnement', perk labels. No string overlap — confirms wrong screen mapping.

### CreatorChannelSetupView
- [color] Price value 9,99€ is mint/green+bold in Figma, but ListRow renders `value` in muted onSurfaceVariant grey with no color override prop — mint price color unachievable via current ListRow.
- [icon] Perk checkmarks are filled green circular badges (white ✓) in Figma; RN renders a bare ✓ Text glyph tinted accent with no circle background/badge — wrong glyph treatment.
- [text] Price default '$9.99' (USD, dot) vs Figma '9,99 €' (EUR, comma), while priceSubtitle says 'TVA incluse' (EU VAT) — currency/locale mismatch in defaults.

### KycCompanyView
- [text] Headline mismatch: Figma 'Informations entreprise' (eyebrow 'VÉRIFICATION') vs RN 'Vérifie ton entreprise' (pill 'TYPE : ENTREPRISE'). Header title also differs: Figma 'Vérification' vs RN 'Paiements business'.
- [missing] RN-only elements absent from Figma: 84x84 hero icon box, lead paragraph, 'TYPE : ENTREPRISE (COMPANY)' pill, and the 'Tu es solo ?' switch-to-Pro-Creator info Banner. Figma has none of these.
- [cta] CTA shape/icon: Figma CTA is a full pill (radius ~999) with a shield icon + 'Continuer la vérification'. RN Button variant=gradient size lg uses atom radius (not 999) and has no leading shield icon; label is 'Vérifier mon entreprise'.

### ManageSubscriptionView
- [text] Header title mismatch — Figma shows 'Abonnements'; RN titleText is 'Gérer mes abonnements' (per fixtures + i18n v2ManageSubscriptionView.json).
- [missing] No platform card rendered — RN has deep-mint account badge (#176A5A white ink), 'ACTIF' status pill, plan name, large price (99 $/mois), renewal line, and outline 'Gérer dans l'App Store' CTA. None present in Figma.
- [missing] No channel-subscription cards — RN renders avatar + creator name + price + status dot/word + chevron + cancel/reactivate CTA per active/canceling sub. Absent in Figma frame.

### MySubscriptionsView
- [dimension] RN renders ONE card per subscription (radius 18, outline border, padding 16). Figma packs both subs as rows inside a single shared card with an internal divider — wrong card structure/grouping.
- [missing] RN stats summary card (two columns: active count + monthly total '169,90 EUR / Par mois') is missing. Figma replaces it with a plain prose subtitle '2 abonnements actifs'.

### PackPurchaseSuccessView
- [icon] Row leading icons render as solid multicolor placeholder squares (purple/blue/orange/mint). RN spec = real icon SLOTs mint-tinted via leadingTint=t.colors.primary. Wrong color + placeholder look, no glyph.
- [color] Primary CTA 'Reserver une seance' gradient drifts teal->blue on the right edge. Canonical Button variant='gradient' = two-tier mint gradient (no blue). Off-brand accent.

### PackageDetailView
- [nav] RN sub-screen uses BackButton (chevron, onSurface). Figma shows a filled grey circular X (close/dismiss modal) top-left — different navigation affordance than the RN back arrow.

### PackagesOwnerView
- [text] Bottom CTA label differs: Figma reads 'Voir l'historique des ventes' (view sales history) but RN bottom Button renders 'Nouveau pack' (addPackageLabel). Different action entirely.
- [cta] Bottom CTA style differs: Figma = outlined mint-border button (style C, no fill, mint text); RN bottom Button uses variant='gradient' (filled mint gradient, white ink). Fill vs outline mismatch.
- [text] Currency mismatch: Figma shows EUR (1 883 €, 269 €, 149 €); RN truth/fixtures use USD ($1,883, $269, $149). Smuppy canonical prices are USD.

### PackagesEditView
- [color] Delete (trash) glyph rendered grey/neutral outline in Figma; RN uses t.colors.danger (red) for the delete affordance. Destructive color cue missing.

### PayoutOnboardingView
- [missing] RN not_started renders a 3-step checklist card (Verifie ton identite / Ajoute ton compte bancaire / Encaisse tes revenus) below the lead; Figma frame shows NO steps card.
- [cta] Figma has TWO bottom CTAs (outline 'En savoir plus' + gradient 'Connecter Stripe'); RN has only ONE gradient CTA ('Commencer la configuration'). Extra secondary outline button + no 'learn more' in RN.

### PlatformSubscriptionView
- [missing] Figma lists 'Badge verifie' as an INCLUDED unlock row, contradicting RN contract where the verified badge is a SEPARATE 14,90$/mois add-on (only the footnote, never an unlock). Implies it is bundled — money/contract error.

### ChannelOwnerView
- [cta] Figma primary CTA is outline (mint border/text, no fill). RN primary is variant=gradient (mint gradient FILL). Missing mint gradient on main CTA.
- [text] Currency mismatch: Figma uses EUR ('9,99 €/mois', '412 €'). RN truth uses USD ($9.99/mois, $412). Smuppy prices are USD.
- [missing] Subscriber-count summary line ('48 abonnés actifs ce mois-ci') present in RN truth (testID subscriber-line) but absent in Figma render.

### CreatorWalletView
- [text] Currency mismatch: RN fixtures use USD '$' with dot decimals ($2,847.50 / +$6.99); Figma shows EUR '€' with comma decimals (2 847,50 € / +6,99 €). Smuppy real prices are USD.
- [text] Stat tiles differ: RN split is 'Disponible'/'En attente' (available vs pending). Figma shows 'Ce mois'/'Total gagné' (+284 € / 12 384 €) — different metric semantics AND strings.

### DataExportView
- [icon] CTA shows a leading flag-like glyph before 'Demander l'export'; RN Button renders children only (no icon prop passed) — extraneous icon not in RN.

### IdentityVerificationView
- [missing] Steps strip shows only 3 steps (Type de pièce / Photo recto / Photo verso); RN has 4 (4th = 'Selfie liveness' liveness selfie). Final KYC step missing in Figma.
- [color] Doc-card icons are off-palette: Passeport glyph is BLUE, Permis glyph is PURPLE. Canonical = mint accent for all card icons (only Carte d'identité icon is mint).

### HelpView
- [missing] Figma omits the search field. RN HelpView renders a controlled search TextInput (surfaceContainerHigh field, clear affordance) in the happy state — core section absent in maquette.
- [missing] Figma omits the contact-support footer CTA. RN renders a mint solid lg Button 'Contacter le support' (ListFooterComponent) — a primary support action is missing.

### MyRatingsSettingsView
- [missing] Figma rows each have a large colored leading icon square (orange/purple/blue/green per ability). RN MyRatingsSettingsView ListRow renders title+subtitle+trailing toggle only — no leading icon/color. Either add leading ability icons or drop them from the maquette.
- [missing] Figma has a bottom 'Comment ça marche' info/help card explaining ratings + 'keep ≥3 abilities visible' rule. RN view has no help/explainer block at all — section absent.

### NotificationsView
- [missing] Filter-tab row (Tout · 12 / Nouveaux fans / J'aime / Peaks) from NotificationsView is absent in the Figma render.
- [header] RN header has mark-all-read + settings icon buttons (headerActions). Figma header shows only back chevron + centered title — both trailing icon actions missing.

### NotificationSettingsView
- [icon] 'Nouveaux fans' icon: RN fixture = ➕ (plus). Figma renders a face emoji — wrong glyph for this row.
- [icon] 'Rappels de session 1:1' icon: RN = ⏰ (clock). Figma renders a calendar/grid glyph — wrong glyph.
- [text] Toggle state mismatch 'Mentions': RN fixture value=false (OFF), Figma shows it ON (mint track).

### PrivacySettingsView
- [icon] Figma icon tiles are empty colored squares; RN renders an emoji glyph inside each tinted square (🌐 ✅ 🙈 📊 🎯 ⬇️ ✏️ 📜). Glyph missing in Figma.
- [missing] RN 'Tes droits' section has a 4th link row 'Utilisateurs bloqués' (value '3'); absent from Figma render (only 3 rights rows shown).

### SecuritySettingsView
- [missing] RN toggle rows (Déverrouillage biométrique on/off pill) and destructive rows (Désactiver le 2FA, Déconnecter in red) have no counterpart in the Figma render.
- [icon] No row icons (shield/key/biometric/device glyphs with mint tint squares) rendered in Figma; RN shows leading tinted icon per row.

### BlockedRegionView
- [missing] Figma is missing the detected-region pill ('Région détectée : France' with 📍) and the compliance notice text. Both are core RN elements that carry the non-color status meaning.
- [text] Title/message strings differ from RN. RN title='Smuppy n'est pas encore disponible ici' / message='Nous ne pouvons pas encore proposer Smuppy dans ta région...'. Figma uses generic 'Indisponible dans ta région' / 'Ce contenu n'est pas accessible... raisons réglementaires' (content-blocked tone, not the Meta-Transparency availability tone).

### EditInterestsView
- [missing] Header title 'Centres d'intérêt' (accessibilityRole=header) is absent in the Figma frame; replaced by a 2/3 progress bar that EditInterestsView does not render.
- [text] Count/hint line mismatch: RN shows count line '{N} sélectionnés' + hint 'Choisis ce qui te passionne...'. Figma shows onboarding hint 'Sélectionne ce qui te branche · au moins 3' with no selected-count text.

### FansListView
- [text] Row subtitle wrong: Figma shows 'Coach · 1.2K fans' (role + follower count). RN row secondary line is the @username handle (e.g. @lea.run). Content mismatch.
- [cta] 'Fan' pill is dark-mint text on a solid mint fill (mint-on-mint, low contrast). RN track CTA is a gradient mint Button with constant WHITE ink (AA). Color/ink not conform.
- [nav] Tabs rendered as bordered selectable pill-chips ('Fans · 24K' / 'Tracking · 412'). RN tab strip is plain text labels 'Fans {n}' / 'Suivi {n}' with a 2px mint underline on the active tab — no pill/border box.

### MatchPageView
- [missing] RN groups players into per-team chip rows (Joueurs → teamA/teamB chips with avatars); Figma collapses this into a single 'Composition' count line with no player chips/avatars — structure diverges.
- [missing] Figma 'Composition' card adds a substitutes count ('3 remplaçants') that has no field in the RN MatchPageView data model (no substitutes concept exists in props/fixtures).

### PlayerCareerCardView
- [missing] RN renders a Summary grid (StatTiles: Note globale/Compétences/Évaluateurs) AND a full ability detail list (ListRows 'Noté par N coéquipiers'). Figma shows NEITHER section — both whole RN sections absent.
- [color] Classic card palette mismatch. RN classic = navy bg #0B1F3A with BLUE accent #6FB5FF (ability labels/role). Figma classic card = near-black bg with MINT-green accents on OVR, role pill, and ability labels.
- [missing] Card chrome elements absent in Figma: no sport line under name (RN cardSport), no top/bottom dividers (cardDivider), and no 'SMUPPY' brand wordmark footer (brandLabel). RN card includes all three.

### EditExpertiseView
- [emoji] Stray placeholder element below the back chevron: a large rounded pill containing a green star/asterisk glyph. Not present in RN (header is back + title + Save only). Looks like an orphan/placeholder node.

### EditBusinessCategoryView
- [dimension] Figma renders chips in a 3-column wrap grid; RN renders a single-column vertical FlatList (full-width stacked chips, gap:10). Structural layout mismatch (chip text overlaps in Figma's grid confirm wrap).
- [color] Selected chip ink inverted: RN selected = SOLID adaptive primary fill + onPrimary WHITE text; Figma selected = light mint tint fill + MINT text + mint border (sober style-C). Opposite fill/ink treatment.

### GoLiveIntroView
- [missing] Features section missing: 'Ce que tu peux faire' title + 4 feature rows (stream/interact/save/track) with mint primarySoft icon chips not rendered.
- [missing] Trial banner missing: 'Période d'essai' label, 'Il reste 42 jours' caption and mint progress bar (trialProgress) absent.
- [cta] Primary CTA mismatch: RN expects gradient 'Démarrer le direct' button (lg, ~h54/radius~28, mint gradient) + Pro-gate panel; Figma has no go-live CTA at all.

### GoLiveView
- [color] Currency mismatch: Figma shows EUR (9,99 €/mois, Pay-per-view · 4,99 €) but RN fixtures/real prices use USD $ (9,99 $/mois, 4,99 $).
- [icon] Preview control left button renders a Pac-Man-like glyph instead of the RN flip-camera icon (🔄 flipIcon). Right effects glyph is a 4-point star vs RN ✨ — wrong glyphs over the camera preview.

### LivePreviewView
- [text] CTA price: Figma shows \"S'abonner · 9,99 €/mois\" (euros, comma) but RN FR default + fixtures use \"S'abonner · $9.99/mois\" (dollar, dot). Currency symbol and decimal format both mismatch.
- [nav] Figma renders a 5-item bottom nav (home/peaks/+/chat/profile) under the paywall. RN LivePreviewView is a fullscreen overlay (stage flex:1, paywall anchored bottom:0) with NO bottom nav — a paid-live paywall overlay should not show tab bar.

### LiveEndedView
- [emoji] Smups stat shows a 👊 fist emoji under '340' in Figma; RN StatTile renders value/label only, no emoji glyph.

### BusinessDiscoveryView
- [color] Selected chip 'Tous · 24km': Figma = light mint-tinted bg + mint border + mint/dark text. RN = solid deep-green #176A5A fill with WHITE text. Selected-chip fill color/style diverges.
- [text] Mixed language: Figma reviews read 'reviews' (EN: 24/156/89 reviews) while header/subtitles are FR ('Découvrir','Salle de sport'). RN FR fixture uses 'avis'. Figma render is inconsistent EN/FR vs RN baseline.

### DisputeCenterView
- [missing] Figma status shown as filled PILL badges ('En cours' orange, 'Résolu' green). RN renders a plain status WORD + dot, no pill/badge background. Badge component missing.
- [missing] Figma has an eyebrow 'LITIGES' (mint caps) + large H1 'Centre de litiges' + count subtitle '2 litiges en cours'. RN has none of these — only a centered header title, no large title block or active-count line.
