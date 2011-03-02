Name:           %{dz_repo}
Version:        %{dz_rpmver} 
Release:        %{_vendor}%{?suse_version} 
Summary:        DevZone Projects Compiler 

Group:          Amusements/Games
License:        GPLv2
URL:            http://dev.openttdcoop.org

Source0:        %{name}-%{version}.tar

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch:      noarch

BuildRequires:  mercurial p7zip unix2dos grf2html %{?dz_requires}

%description
Build script for #openttdcoop DevZone projects

%prep
%setup -qn %{name}
# update to the tag, if not revision
[ "$(echo %{version} | cut -b-1)" != "r" ] && hg up %{version}

%build                                                                                                                                                                                                     
make %{?_smp_mflags} bundle_zip bundle_src ZIP="7za a" ZIP_FLAGS="-tzip -mx9" 1>%{name}-%{version}-build.log 2>%{name}-%{version}-build.err.log                                                                       

for i in $(ls -1 sprites/nfo/lang/ | grep '.pnfo$' | grep -v '.new.' | grep -v 'cleanup' | grep -v 'nfo_lang' | grep -v 'untranslated' | grep -v 'remove'); do 
  ./scripts/check_language.sh $i >$i.log
  [[ $(cat $i.log | wc -l) -lt 4 ]] && rm $i.log
done

grf2html -o grf2html *.grf 1>%{name}-%{version}-grf2html.log 2>&1                                                                                                                                                      
                                                                                                                                                                                              
%install                                                                                                                                                                                                   
                                                                                                                                                                                                           
%check                                                                                                                                                                                                     
                                                                                                                                                                                                           
%clean                                                                                                                                                                                                     
                                                                                                                                                                                                           
%files                                                                                                                                                                                                     
                                                                                                                                                                                                           
%changelog    
