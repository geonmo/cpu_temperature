Name: ganglia-plugin-cpuheat		
Version:	0.2
Release:	1%{?dist}
Summary:	This problem support the cpu temperature to ganglia

Group:		GSDC
License:	GPL
URL:		none
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	/bin/rm, /bin/mkdir, /bin/cp
Requires:	lm_sensors >= 3.4.0 
Requires:	ganglia
Requires:   ganglia-gmond-python
Requires:   ganglia-gmond
Requires:   /bin/bash
Requires:   /usr/sbin/sensors-detect
Requires:   systemd

%description
sensor?

%prep
/usr/sbin/sensors-detect --auto
#%setup -q




%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib64/ganglia/python_modules
mkdir -p $RPM_BUILD_ROOT/etc/ganglia/conf.d

cp cpu_temp.py $RPM_BUILD_ROOT/usr/lib64/ganglia/python_modules/
cp cpu_temp.pyconf $RPM_BUILD_ROOT/etc/ganglia/conf.d

%clean
rm -rf $RPM_BUILD_ROOT



%files
%attr(0644,root,root)/usr/lib64/ganglia/python_modules/cpu_temp.py
%attr(0644,root,root)/usr/lib64/ganglia/python_modules/cpu_temp.pyc
%attr(0644,root,root)/usr/lib64/ganglia/python_modules/cpu_temp.pyo
%attr(0644,root,root)/etc/ganglia/conf.d/cpu_temp.pyconf

#%doc



%changelog
* Mon Mar 03 2020 Geonmo Ryu <geonmo@kisti.re.kr> - 0.2
- Add a requirement about systemd
* Mon Jan 21 2019 Geonmo <geonmo@kisti.re.kr> - 0.1
- Initial RPM
