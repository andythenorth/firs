import firs
from industry import Industry

# Find which industries dislike which other industries
dislikes = {}
for ind in firs.registered_industries:
    lc = ind.location_checks
    if lc is None:
        dislikes[ind] = set()
        continue

    dislikes[ind] = set(lc.incompatible)

# Find what each industry produces and accepts
accepting_inds = {} # Map of cargo to list of accepting industries
producing_inds = {} # Map of cargo to list of producing industries
for ind in firs.registered_industries:
    if ind.default_industry_properties.accept_cargo_types == None:
        print(ind.default_industry_properties.accept_cargo_types)
        raise Exception(ind.id)
    if len(ind.default_industry_properties.accept_cargo_types) == 0:
        print("Warning: Industry \"{}\" does not accept any cargo".format(ind.id))

    for ct in ind.default_industry_properties.accept_cargo_types:
        acc_inds = accepting_inds.get(ct)
        if acc_inds is None:
            accepting_inds[ct] = [ind]
        else:
            acc_inds.append(ind)

    if len(ind.default_industry_properties.prod_cargo_types) == 0:
        print("Warning: Industry \"{}\" does not produce any cargo").format(ind.id)

    for ct in ind.default_industry_properties.prod_cargo_types:
        prod_inds = producing_inds.get(ct)
        if prod_inds is None:
            producing_inds[ct] = [ind]
        else:
            prod_inds.append(ind)

all_cargoes = set(accepting_inds).union(producing_inds)

conflicts = {} # Map of cargo to pairs of producing -> accepting conflicts
for ct in all_cargoes:
    if ct in accepting_inds:
        if ct in producing_inds:
            conflicts[ct] = (producing_inds[ct], accepting_inds[ct])
        else:
            print("Cargo {} is never produced (accepted by {})").format(ct, ",".join(ai.id for ai in accepting_inds[ct]))
    else:
        if ct in producing_inds:
            print("Cargo {} is never accepted (produced by {})").format(ct, ", ".join(pi.id for pi in producing_inds[ct]))
        else:
            assert False # Should not happen as 'all_cargoes' is derived from usage.

for ct, (prod_inds, accept_inds) in conflicts.items():
    for p in prod_inds:
        pdis = dislikes[p]
        for a in accept_inds:
            adis = dislikes[a]

            if a.id not in pdis:
                msg = "Accepting industry \"{}\" can be close to producer \"{}\", transporting {}"
                print(msg.format(a.id, p.id, ct))

            if p.id not in adis:
                msg = "Producing industry \"{}\" can be close to accepting \"{}\", transporting {}"
                print(msg.format(p.id, a.id, ct))

