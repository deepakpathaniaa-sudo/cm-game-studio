// Shared Supabase client — included in every page
const SUPABASE_URL = 'https://xoxjcpbruryjcqonzwag.supabase.co';
const SUPABASE_KEY = 'sb_publishable_Tu7LS4Mjd0YKmYVMIg4Gag_oK4ih9Se';
const sb = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);

const ROLE_ROUTES = { student:'/student', instructor:'/instructor', parent:'/parent', admin:'/admin' };

async function getProfile() {
  const { data:{ user } } = await sb.auth.getUser();
  if (!user) return null;
  const { data } = await sb.from('profiles').select('*').eq('id', user.id).single();
  return data ? { ...data, email: user.email } : null;
}

async function requireRole(...roles) {
  const { data:{ session } } = await sb.auth.getSession();
  if (!session) { window.location.href = '/'; return null; }
  const profile = await getProfile();
  if (!profile || !roles.includes(profile.role)) { window.location.href = '/'; return null; }
  return profile;
}

async function logout() {
  await sb.auth.signOut();
  window.location.href = '/';
}
