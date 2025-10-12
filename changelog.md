Changelog
=========


--------------
5.0.0 Release
--------------


**FIRS 5.0.0 is not savegame-compatible with any previous version of FIRS.**


*Changes*

- significantly reworked Steeltown
    - provide a more diverse range of uses for steel
    - represent steel by the more common physical form (billets, ingots, slab, bars, etc), rather than the specific grade of steel (carbon, stainless etc)
    - add more end-stage cargos alongside Vehicles, including Concrete Products, Goods, Hardware and Pipework
    - accept more cargos at Port and Wharf to make it easier to boost production
- added cargos
    - Billets & Blooms
    - Concrete Products
    - Ferroalloys
    - Forgings & Castings
    - Hardware
    - Merchant Bar
    - Nitrogen
    - Plant & Machinery
    - Pumps & Valves
    - Rebar
    - Seals, Hoses & Belts
    - Steel Ingots
    - Steel Plate
    - Steel Slab
    - Steel Tube
    - Storage Tanks & Pipework
    - Structural Steel
    - Tyre Cord
    - Welding Consumables
- removed cargos
    - Alloy Steel
    - Carbon Steel
    - Ferrochrome
    - Steel Sections
- renamed cargos
    - Pipe now Steel Pipe
    - Stone now Aggregates
    - Steel Sheet now Steel Sheet & Strip
    - Vehicle Engines now Engines & Driveline
- added industries
    - Appliance Factory
    - Concrete Plant
    - Elastomer Products Plant
    - Metal Works
    - Pipe Shop
    - Plate Mill
    - Power Systems Factory
    - Precision Parts Plant
    - Section & Bar Mill
    - Steel Forge & Foundry
    - Strip Mill
    - Tracked Machine Factory
    - Tube & Pipe Mill
    - Wire Rod Mill
- removed industries
    - Bulk Terminal
    - Component Factory
    - Metal Workshop
    - Sheet and Pipe Mill
    - Wire and Section Mill
- reworked port-type industries
    - can now locate on many more coast locations, so easier for OpenTTD to place them during map generation or during gameplay
    - unfortunately can still be difficult for player to place in some circumstances
    - sprites and layouts reworked for both Port and Wharf
    - layouts reworked for Liquids Terminal
- added more objects for many more industries, including
    - additional decor objects for some industries, not otherwise used in the industry layout
    - empty tile objects for many industries, for convenient building of gaps and spaces
- 'Gung Ho' production is now 250% by default, not 300% (can still be adjusted by parameter)
- removed cobble ground type and convert industries using it to alternative ground types


*Docs*

- update code reference info about deps and python version
- mysys no longer relevant, remove mention of it from code reference page


*Fixes*

- make sure always Cryo Plant prospecting always succeeds (as long as there is a suitable place for it on the map)
- Lime Kiln purchase cost was too low


*Codechanges*

- change cargo classes to FRAX scheme
- switch lang files to TOML format
- make use of increased object limit in OpenTTD
- track cargo and industry sprite completion
- reduce python boilerplate by using dynamic imports for cargo, economies and industries
- cargos no longer need specific order to avoid breaking house cargo acceptance/production (as of OpenTTD #11378)
- reorganise src directories
- add FIRS GS generation


--------------
4.16.0 Release
--------------


*Changes*

- add more objects


*Codechanges*

- adjust cargo classes to FRAX scheme


--------------
4.15.1 Release
--------------


*Fixes*

- objects that use baseset sprites weren't showing them in Object Selection UI (applies to Sawmill, Power Station etc)


--------------
4.15.0 Release
--------------


*Changes*

- added ground sprites for multi-tile objects in Object Selection window
- removed display of fences for all objects in Object Selection window (seems fine)
- build selected industry types in specific areas of the map for Basic Temperate and Basic Tropic


--------------
4.14.1 Release
--------------


*Changes*

- added correct building sprites for multi-tile objects in Object Selection window
    - still misses ground tile and fences
    - positioning of sprites is less than ideal in some cases


--------------
4.14.0 Release
--------------


**FIRS 4.14.0 is not savegame-compatible with any previous version of FIRS.**


*Changes*

- added animation support for objects, if the object is animated
- added snow support for objects, if the object provides snow sprites


--------------
4.13.0 Release
--------------


*Changes*

- added magic fences to objects
    - these work the same as existing industry fences
    - the object defines whether fences show or not by default
    - fences will hide if the adjacent tile is an industry, an object, or a station tile
- added object detection to industry magic fences
    - industry fences will now hide if the adjacent tile is an object, as well as the existing checks for industry and station tiles
- magic fences may hide sometimes in unwanted/unexpected ways
    - for example, fences will hide if the adjacent tile is a lighthouse or transmitter, or similar scenic object types
    - there is no current way to solve this in the grf spec, so we'll live with it, it's probably fine
- renamed 'Kaolin' to 'China Clay', as it's the more common term in British English


*Codechanges*

- refactored some internals which should have no visible gameplay effect, but have probably introduced bugs (version number is unlucky 13)
    - spritelayouts now provision their tile ID reference directly, not via the industry layout
    - industry economy variations now provisioned by a defined init method, not via directly rewriting properties of the economy variation object after init
    - refactored OR logic of industry location checks
    - support for creating industries in defined map regions ('biomes') - not used currently, no gameplay effect
    - removed some leftover elements from economy experiments
    - make snow support explicitly defined instead of assuming every industry has snow, this allows the removal of many redundant spritesheets


--------------
4.12.1 Release
--------------


*Fixes*

- Gung-Ho % parameter overlapped with Landscaping Objects parameter, causing Gung-Ho to have incorrect values


--------------
4.12.0 Release
--------------


**FIRS 4.12.0 is not savegame-compatible with any previous version of FIRS.**


*Changes*

- added support for multi-tile objects (no longer limited to 1x1)
    - converted all objects that are more than 1x1 to multi-tile layouts
    - note that Object Selection window is still limited to showing these objects as 1x1 with sliced sprites, but they will be correct when built
- changed how colours are chosen for industries and objects
    - each industry type will now take its random colour from the nearest town, not global random
    - objects matching the industry type will use the same colour as the industry type when built in the same town
    - notes:
        - objects will use company colour in the Object Selection window, and may show a different colour when built
        - object colour may not match a nearby industry if they are built in the catchment of a different nearby town


--------------
4.11.0 Release
--------------


**FIRS 4.11.0 is not savegame-compatible with any previous version of FIRS.**


*Changes*

- grouped FIRS landscaping objects into classes per industry (experimental)
- split most industry buildings / assets into separate objects, instead of using views within an object
- added better control over order of objects (but not order of object views)
- if there are 3 views for an object, repeat the 3rd view to make a 4th, as the spec does not support having 3 views
- forced 'FIRS landscape objects' parameter to default to 'On'
- the remaining limitations from FIRS 4.10.0 still apply to FIRS landscaping objects


--------------
4.10.0 Release
--------------


**FIRS 4.10.0 is not savegame-compatible with any previous version of FIRS.**


*Changes*

- switched Assembly Plant to use 'outpost' layout
- (experimental) added a set of FIRS landscaping objects, which players can place to make certain industries appear larger
    - landscape object have no gameplay effect
    - landscaping objects can be turned on or off via parameter
    - this is the first version of landscaping objects, there may be bugs
    - limitations /
        - not all industry tiles have equivalent objects (for a range of reasons)
        - no objects can build on water
        - no objects can build on steep slopes
        - no objects feature animation, this includes smoke which is missing in all cases
        - no objects have snow sprites
        - no objects show fences
        - all objects are currently 1x1 tiles
        - some objects have sliced sprites and must be combined precisely with other objects to get the correct appearance
        - any objects using company colour will use the player company colour (no method exists to match colour to an industry)
        - by design, objects are only available in the same FIRS economies as their industry
        - by design, objects have no date restrictions
        - objects cannot easily be made free to build, but they are set to the lowest possible build cost
        - objects are not ordered alphabetically in the object menu
        - order of object views is not yet designed, they come as they are
        - changes are likely to be made to how objects are provided in forthcoming release
    - this is not intended to replace existing grfs such as 'FIRS and CHIPS objects', which are more full-featured
        - it just happens be very easy and very little work to make FIRS provide these objects, within the limits above


*Docs*

- updated some industry docs images


*Codechanges*

- renamed some industries and cargos in code to be consistent with their names in game


-------------
4.9.0 Release
-------------


**FIRS 4.9.0 is not savegame-compatible with any previous version of FIRS.**


*Changes*

- adjusted position of some outpost layouts relative to main industry layout
    - provides for more useful / flexible routing, following gameplay testing


*Docs*

- fixed some missing heading separators


-------------
4.8.0 Release
-------------


**FIRS 4.8.0 is not savegame-compatible with any previous version of FIRS.**


*Changes*

- reworked Electric Arc Furnace
    - entirely new sprites
    - new larger layouts using 'outpost' approach
- tweaked fences at Basic Oxygen Furnace so that the casting line is always fenced, even if a station is adjacent
- added ECS Basic Vector II to list of incompatible grfs


*Fixes*

- removed pink scaffolding pixels from Basic Oxygen Furnace, as they are hidden with original baseset, but show up with OpenGFX


*Docs*

- note in docs that since OpenTTD 12.0, FIRS is supported by default vehicles


*Translations*

- translation updates (thanks translators)



-------------
4.7.0 Release
-------------


**FIRS 4.7.0 is not savegame-compatible with any previous version of FIRS.**


*Changes*

- animated casting plant for Basic Oxygen Furnace


-------------
4.6.0 Release
-------------


**FIRS 4.6.0 is not savegame-compatible with any previous version of FIRS.**


*Changes*

- added larger layouts using 'outpost' approach for Basic Oxygen Furnace
- improved Slag Grinding Plant sprites and layouts
- improved layouts for Sheet and Pipe Mill, Wire and Section Mill
- added detail to Blast Furnace sprites (2TallTyler)
- improved incompatible industries checks (2TallTyler)


*Translations*

- translation updates (thanks translators)


-------------
4.5.0 Release
-------------


**FIRS 4.5.0 is not savegame-compatible with any previous version of FIRS.**


*Changes*

- added larger layouts using 'outpost' approach for following industries
    - Chlor-alkali Plant
    - Coke Oven
    - Sheet and Pipe Mill
    - Wire and Section Mill
    - these are experimental, and intended to ease station placement for certain industries that produce 3 or more cargos


*Codechanges*

- various Makefile tweaks
- experiments in town happiness / town economy and primary industry production increases, all feature-flagged off currently as unfinished


-------------
4.4.0 Release
-------------


**FIRS 4.4.0 is not savegame-compatible with any previous version of FIRS.**


*Changes*

- improved co-location checks for certain industry types:
    - removed exemptions to co-location checks for these industry types when generating map (exceptions were needed to avoid these industries failing to generate)
    - applies to:
        - Cement Plant
        - Chemical Plant
        - Fishing Harbour
        - Food Processing Plant
        - Lime Kiln
        - Paper Mill
- reduce fund cost of Cryo Plant, reflecting that it has fixed production


*Translations*

- translation updates (thanks translators)


*Codechanges*

- split Steel Mill from Blast Furnace into separate industry (preparatory to possibly changing sprites later)
- reworked secondary production
    - switched span calculation from 90 days to 27 cycles of the 256-tick production cb
    - approach is consistent with how primaries handle production
    - should have no visible effect for most players; any observable change should be in the player's favour
- reworked primary production randomisation
    - stopped randomising production_level var at start
    - added a separate var for randomising initial production
    - this is preparatory to using production_level for permanent primary production changes (mechanic for that not designed yet)
- shuffled some industry IDs so that keystone industries are built in correct sequence at map gen (which builds industry types sequentially, lowest ID first)


-------------
4.3.0 Release
-------------


**FIRS 4.3.0 is not savegame-compatible with any previous version of FIRS.**


*Changes*

- reworked primary industry supplies handling (including port-type industries where all input cargos count as 'supplies')
    - **this is not a significant gameplay change, it just removes some inconsistencies**
    - applied consistent approach to 'deliver every 3 months', using a window of 93 days (27 production cycles on the 256-tick callback)
    - dropped use of exact date calculations and monthly production callback, which could produce inconsistent results in some cases
    - synchronised update of industry window text indicating 'Supplied' and 'Current production'
        - industry window text should now change on delivery of cargo in both cases, which feels more natural
        - occasionally latency in OpenTTD might still cause these two text indicators to be briefly out of sync


*Translations*

- translation updates (thanks translators)


-------------
4.2.1 Release
-------------


*Fixes*

- adjust location checks added in 4.2.0 to make it much less likely that some types will never be built on small maps / low industry setting


-------------
4.2.0 Release
-------------


**FIRS 4.2.0 is not savegame-compatible with any previous version of FIRS.**


*Changes*

- reworked location checks for certain processing industries so they always locate within reasonable distance of at least one other industry type in their chain
    - checks for primary (input) sources added for:
        - Cement Plant
        - Cider Mill
        - Copper Refinery
        - Dairy
        - Food Processing Plant
        - Lime Kiln
        - Paper Mill
        - Sawmill
    - added Fish Farm to Fishing Harbour, which previously only checked for Fishing Grounds
    - added Coal Mine to Coke Oven, which previously only checked for Blast Furnace
    - added Electric Arc Furnace and Basic Oxygen Furnace to Slag Grinding Plant, which previously only checked for Blast Furnace
    - most other processing industries do not use this location check by design, and may require cargo to be transported a long distance, for gameplay reasons ;)
- increase spacing between industries to 2 tiles (was 1 tile)


*Codechanges*

- rewrote location check handling to use procedures
- split Cider Mill into a separate industry from Brewery, for simplicity of location checks


-------------
4.1.0 Release
-------------


**FIRS 4.1.0 is not savegame-compatible with any previous version of FIRS.**


*Changes*

- renamed Wood cargo to Logs
    - Wood was repeatedly conflated with Lumber/Timber
    - Logs is more obvious
    - cargo label remains WOOD as it is so widely supported
- Scrap Yard/Junk Yard requires town population of at least 400 when game is placing Scrap Yards
    - this improves gameplay with Scrap Yards, as the production depends on town population
    - player can place Scrap Yards anywhere when buildiing industry manually


-------------
4.0.1 Release
-------------


*Docs*

- improved cargoflow diagrams to show town destinations that were missing from FIRS 4.0.0 cargoflow diagrams


*Translations*

- translation updates (thanks translators)


-------------
4.0.0 Release
-------------


*Steeltown*

- reworked completely, Steeltown is a much more intense, highly-connected economy
    - Carbon Steel is a key cargo
        - there are two routes to produce it, the Blast Furnace route, which depends on many primary inputs
        - the Electric Arc Furnace route, which depends highly on scrap production, which depends on the population of towns
    - there are many more steel industry processes and end products represented
    - vehicles production process is also more detailed
- added cargos
    - Alloy Steel
    - Aluminium
    - Carbon Black
    - Carbon Steel
    - Cast Iron
    - Cement
    - Cleaning Agents
    - Coal Tar
    - Electrical Parts
    - Ferrochrome
    - Glass
    - Sodium Hydroxide
    - Oxygen
    - Paints & Coatings
    - Plastics
    - Potash
    - Stainless Steel
    - Steel Sections
    - Steel Sheet
    - Steel Wire Rod
    - Tyres
    - Vehicle Engines
- removed cargos
    - Petroleum Fuels
    - Copper
    - Steel
    - Electrical Machines
- added industries
    - Body Plant
    - Builders Yard
    - Carbon Black Plant (new sprites)
    - Component Factory (new sprites)
    - Cryo Plant (new sprites)
    - Engine Plant (new sprites)
    - Potash Mine
    - Sheet and Pipe Mill (new sprites)
    - Vehicle Distributor
    - Wire and Section Mill (new sprites)
- Chlor-alkali Plant replaces Chemical Plant
- removed industries
    - Foundry
    - Steel Finishing Plant
    - Metal Workshop
    - Port
    - Vehicle Dealer
- Scrap Yard production amount now depends on town population (grow town to increase production)
- improved sprites for Slag Grinding Plant
- rebalanced industry probabilities
    - most secondary industries in Steeltown will only build at game start, not during gameplay
    - this avoids the game spamming the map with new secondary industries that are unlikely to be served
    - this increases the chance of the game building useful new primary industries


*Extreme*

- removed Extreme economy from FIRS
    - the future of 'big' economies in FIRS is detailed themes (industry chains or world regions)
- for the most interesting current FIRS gameplay, use Steeltown, which focusses on highly connected industry chains
- meanwhile, if you want a 'big general economy':
    - try an alternative industry, options include grfs based on FIRS, like XIS or Auz Industries
    - or make your own version of FIRS, many people have done this now, code is on github https://github.com/andythenorth/firs


*Temperate Basic*

- renamed Clay to Kaolin
- removed Bulk Terminal
- adjusted Port cargos
    - added Kaolin to accepted
    - removed Alcohol from accepted
    - added Chemicals and Farm Supplies to produced
- Scrap Yard production amount now depends on town population (grow town to increase production)


*Arctic Basic*

- reworked cargo and industry chains
- removed Trading Post
- removed Furniture Factory
- replaced Bulk Terminal with Wharf
- added Fish Farm industry
- added Ammonia cargo
- added Potash cargo
- removed Alcohol cargo
- removed Goods cargo


*Tropic Basic*

- removed Bulk Terminal, moved its cargos to Port


*In a Hot Country*

-  no changes to industry chains or cargos


*General Changes*

- reduced overlap of cargos on cargo payment rate chart in-game
- removed option for secondary industries to close
- improved ground tile sprites for multiple industries
- increased sizes of layouts for multiple industries
- added BSPI to list of incompatible grfs
- added CZTR Engines (Diesel, Electric, EMU, Steam) to list of incompatible grfs
- added North Korean Industry Set (various versions) to list of incompatible grfs
- added XIS to list of incompatible grfs
- renamed Copper Refinery to Copper Smelter
- removed all intro date limitations except Oil Rig
- adjusted cargo colours to account for legibility against the black cargo payment chart introduced in OpenTTD 1.11


*Docs*

- improved cargoflow diagrams


*Fixes*

- prevent Oil Rig, Dredging Site and Fishing grounds building on coast of small islands (frosch)
- prevent flickering sprites at Coke Oven


*Translations*

- multiple translation updates (thanks translators)


*Codechanges*

- moved to git
- reworked all production-related industry code to use OpenTTD's improved spec for industry cargos (16-in, 16-out per industry)
    - note for those forking: FIRS caps cargos to 8-in, 8-out for both gameplay reasons, and because production code maths relies on not dividing by more than 8, to avoid very small fractional cargo production
- introduced nml procedures, eliminating many blocks of repeated nml, improving compile times
- improved compile / Makefile


--------------
3.0.12 Release
--------------


*Docs*

- note that nml 0.4.5 or newer is needed for compiling FIRS


*Translations*

- updated


--------------
3.0.11 Release
--------------


*Fix*

- match units_of_cargo with items_of_cargo (frosch)


*Docs*

- updated svg-pan-zoom plugin for industry chain viewing


--------------
3.0.10 Release
--------------


*Docs*

- fix broken links in economies page


*Translations*

- updated


-------------
3.0.9 Release
-------------


*Codechange*

- improved how 'make install' handles copying the grf to install location


*Translations*

- updated


-------------
3.0.8 Release
-------------


*Fix*

- 3.0.7 didn't show the version number correctly


-------------
3.0.7 Release
-------------


*Fix*

- 3.0.6 unintentionally broke industry availability, now fixed


*Docs*

- more accurate licensing information


-------------
3.0.6 Release
-------------


*Docs*

- cargos, economies and industries can now be deep linked


*Translations*

- updated


-------------
3.0.5 Release
-------------


*Fixes*

- display correct version number in grf name


*Codechanges*

- cleaned up makefile and build scripts
- switched to generated lang files
    - dropped custom_tags.txt
    - STR_EMPTY now only provided once, eliminating a proven source of bugs coming in from translated lang files


-------------
3.0.4 Release
-------------


*Translations*

- multiple languages updated


-------------
3.0.3 Release
-------------


*Translations*

- multiple languages updated


-------------
3.0.2 Release
-------------


*Fixes*

- Vehicle Dealer should not have an intro date set


*Translations*

- multiple languages updated


-------------
3.0.1 Release
-------------


*Docs*

- show cargo classes in code reference page


*Translations*

- multiple languages updated


-------------
3.0.0 Release
-------------


**FIRS 3.0.0 is not savegame-compatible with any previous version of FIRS.**

FIRS 3.0.0 requires OpenTTD 1.7.0 or newer.


*Improved Economies*

- 'Arctic Basic' economy
    - totally reworked, inspired by Finland, Northern Canada and Northern Siberia
    - mixed economy, based on natural resources extraction and processing
    - multiple new chains and cargo types, including Explosives, Peat, Sulphur and Zinc
    - new industries include Herding Co-op and Peatlands
    - includes Fish as important food source
- 'Steeltown' economy
    - highly industrial economy, dominated by Iron and Steel chain
    - multiple new chains and cargo types, including Acid, Cement, Chlorine, Coke, Electrical Machines, Limestone, Pig Iron, Pipe, Quicklime, Salt, Soda Ash, Slag and Zinc
    - new industries include Basic Oxygen Furnace, Coke Oven, Soda Ash Mine and Electric Arc Furnace
    - a complex economy with 31 cargos and 25 industries
    - highly focussed on industrial production
    - most chains connect to ultimately produce Vehicles
    - use with any climate


*Improved Industries*

- new industry types:
    - Basic Oxygen Furnace
    - Coke Oven
    - Electric Arc Furnace
    - Farm
    - Foundry
    - Farm / Mixed Farm
    - Herding Co-op
    - Limestone Mine
    - Peatlands
    - Slag Grinding Plant
    - Soda Ash Mine
    - Vehicle Dealer
- improved industry graphics and layouts:
    - Coffee Estate
    - Dredging Site
    - Forest
    - Fruit Plantation
    - Orchard and Piggery
    - Paper Mill (DanMacK)
    - Pyrite Mine
    - Rubber Plantation
    - Vineyard
- Diamond Mine: no longer uses graphics from base set, and has additional layouts
- Fishing Grounds / Fishing Harbour:
    - better clustering and co-location behaviour for this chain
    - where possible, Fishing Harbours will be built within a sensible distance of Fishing Grounds
    - this isn't always possible, good luck!
- Iron Ore Mine: no longer uses graphics from base set, and has additional layouts
- Fertiliser Plant:
    - renamed to Ammonia Plant
    - now produces Engineering Supplies (civil explosives) in addition to Farm Supplies
- Lime Kiln: production ratios improved, industry output was previously nerfed, not intentionally
- Metal Fabrication Plant:
    - name varies by economy, either Metal Fabrication Plant or Steel Finishing Plant
- Mixed Farm:
    - name varies by economy, either Farm or Mixed Farm
- Quarry:
    - minor tweaks to appearance of sand
- Steel Mill
    - name varies by economy, either Blast Furnace or Steel Mill
    - Blast Furnace variant requires Coke, Iron Ore, Limestone, produces Pig Iron and Slag
    - Steel Mill variant unchanged, requires Coal, Iron Ore, Scrap Metal, produces Metal or Steel
- Trading Post
    - name varies by economy, either Trading Post or Wharf
- Vehicle Factory
    - renamed to Assembly Plant


*Improved Cargos*

- new cargo types:
    - Acid
    - Cement
    - Chlorine
    - Coke
    - Electrical Machines
    - Explosives
    - Fertiliser
    - Kaolin
    - Limestone
    - Peat
    - Pig Iron
    - Pipe
    - Quicklime
    - Salt
    - Slag
    - Soda Ash
    - Steel
    - Sulphur
    - Vehicle Bodies
    - Zinc
- Chemicals:
    - increase cargo weight
- Packaging:
    - renamed from Manufacturing Supplies to avoid confusion between this ordinary cargo and Engineering Supplies / Farm Supplies which have special behaviour
    - uses 'tonnes' (or equivalent localised weight) as unit, rather than 'crates'
- Vehicle Parts:
    - removed incorrect 'express' cargo class
- Vehicles:
    - now uses 'tonnes' (or equivalent localised weight) as unit, rather than 'vehicles'
    - simpler for vehicle newgrf authors to deal with, no special treatment needed for Vehicles cargo


*General Improvements*

- reworked industry window text for processing industries
    - dropped 'produces x output per y delivered' text
    - was hard to understand, frequently had mistakes, and made much work for translators
    - now simplified, taking advantage of new features in OpenTTD 1.7.0
    - cargos are simply shown as 'required'
    - 'supplied' will be shown if a cargo has been delivered within the last 90 days
- industries accepting Packaging (previously Manufacturing Supplies):
    - these industries now use same production boost behaviour as all other processing industries when combining cargo
    - previously these industries had special boost behaviour which was hard to explain
    - Packaging only available in Extreme economy
    - Packaging dropped from some industries entirely
- tweaks to industry probabilities for game balance and consistency
- primary industry production levels
    - adjusted production levels at some primary industries for game balance
    - adjusted initial randomisation of these production levels for game balance
- distance checks to incompatible industries now applied consistently
- adjusted clustering behaviour for some primary industries
- Brewery, Flour Mill, Hotel and Junk Yard now check for nearby houses, instead of distance to town sign, this will improve game placement of these industries in large cities
- industry 'nearby station' names are expanded and reworked
    - more industries set unique names for nearby stations
    - existing names reworked
- adjusted all cargo colours:
    - all cargo colours now unique within FIRS
    - each cargo now uses same colour everywhere (charts, station list, cargo flow view) etc.
- adjusted multiple cargo payment curves
    - fix issue where some cargos overlapped each other on cargo payment chart in-game
    - rebalance some cargos for gameplay reasons
- adjusted cargo weights
- rework of industry map colours for better legibility on all 3 map colours (green, dark green, violet) - based on work by Frosch
- added checks for incompatible 'OpenGFX+Industries' and 'Improved Oil Rig Layout' grfs
- adjusted order of economies in parameter menu and docs


*Online Docs*

- text now more helpful for players who are new to FIRS
- improved readme, removing confusing and/or outdated info, and linking to main docs
- Cargos page shows hints about many cargos, to aid vehicle set authors
- Code Reference page shows cargo colours and industry map colours
- Industries page updated with images for new and changed industries
- improved cargo-flow graphs in Economies page
- zoom-and-pan tools to view 'larger' version of cargo-flow graphs (may not work in all browsers, sorry, 3rd-party plugin for this is not 100% reliable)
- docs no longer show cargos that are not used (including Sugar and Sugarcane)
- much more variety in randomised banner images for docs
- upgrade UI library to Boostrap 3
- all pages now use a responsive grid and should work across a wide range of devices
- page layouts redesigned to be more legible and more visually appealing


*Translations*

- multiple languages updated


*Codechanges*

- grfid bumped, v3 is different enough to v2 to justify a new grfid
- improved/fixed display of repo revision in filenames etc
- move lang dir into src for consistency with Iron Horse etc
- new Makefile, much simplified (Alberth)
- remove all use of C-Pre-Processor templates
    - FIRS templating is now 100% python
    - no longer requires GCC-compatible compiler to build FIRS
- only render extra text switches for economies where industry is active (aids compile speed)
- only render 'if economy=x' when needed, saving ~1k lines in output, and slightly faster compile
- only include construction states in spritelayout if needed
- don't set zextents, it's not useful, and may have caused some sprite flickering bugs which now seem resolved
- remove secondary industry debug text; use the newgrf debug to read storages instead
- processing industries with two outputs now have option to produce in ratios other than 50:50
- don't set multiple unnecessary properties for industries and cargos
- fixed minor linting issues found by pyflakes
- removed files and imports for some unused industries and cargos
- rename templates on the filesystem for consistency and ease of navigation
- clean up usage and documentation of industry permanent storage
- remove manually declared ids from spritesets, much less boilerplate and find-replace for industry spritsets
- don't fail silently if tile numeric IDs are not defined; fix a bunch of missing tile numeric IDs
- minor code refactoring in many other places, simplifying where possible
- GPL notice is not required imho for every source file, remove them widely
- pep8 some python files
- magic templates:
    - for industries with trees, including terrain and slope support
    - for harbours
- automated incompatible industry checks
- automated guard against some cases where cargos could be missing
- require_houses_nearby check circular tile search range increased to 7 (and uses automated generator for the ranges)
- set random_sound_effects to empty array to prevent spurious sounds due to default industry properties
- Metal cargo label now 'METL' not 'STEL', cargo labels must be unique per cargo, cannot be reused inside FIRS


--------------
2.1.5 Release
--------------


*Translations*

- updated
- translator credits: http://bundles.openttdcoop.org/firs/releases/LATEST/credits.txt


--------------
2.1.4 Release
--------------


*Translations*

- updated
- translator credits: http://bundles.openttdcoop.org/firs/releases/LATEST/credits.txt


--------------
2.1.3 Release
--------------


*Fixes*

- wrong output in some economies for secondary industries with two output cargos


*Translations*

- multiple languages updated


--------------
2.1.2 Release
--------------


*Translations*

- multiple languages updated


--------------
2.1.1 Release
--------------


*Translations*

- multiple languages updated


--------------
2.1.0 Release
--------------


*Changes*

- new graphics and layouts for Manganese Mine


*Fixes*

- Stockyard had wrong unit for livestock extra info string


*Translations*

- multiple languages updated


--------------
2.0.3 Release
--------------


*Translations*

- multiple languages updated


--------------
2.0.2 Release
--------------


*Fixes*

- Metal Workshop production ratios wrong
- Smithy Forge production ratios wrong


*Translations*

- multiple languages updated


--------------
2.0.1 Release
--------------


*Changes*

- reduce port-type industries supply requirements to 8x parameter setting, not 10x (10x is too hard)
- reduce fund cost of Supply Yard


*Fixes*

- make Copper cargo colour different to Wool in industry chain, cargo payment chart
- Plastics Plant had wrong string in Arctic Basic economy


*Translations*

- multiple languages updated


--------------
2.0.0 Release
--------------


"Better, faster, stronger."

**FIRS 2.0.0 is not savegame-compatible with any previous version of FIRS.**


*Improved Economies*

- 'Temperate Basic' economy
    - added Fish chain, it's important for South West UK, which is the inspiration for this economy
    - adjusted Steel Mill and Metal Workshop intro dates to 1800, fixing broken metal cargo chain before 1850
- 'Arctic Basic' economy
    - totally reworked, inspired by Scandinavia (previously generic sub-Arctic regions)
    - highly industrial economy, dominated by Chemicals chain
    - recommended start date: 1950
    - multiple new chains, including Pyrites, Vehicles and Vehicle Parts chains
- 'Tropic Basic' economy
    - partially reworked, inspired directly by Argentina, Chile and Peru (previously generic South American)
    - this economy focuses mostly on agriculture, and a couple of extractive industry types
    - removed Bauxite and Vehicles chains
    - added Alcohol, Copper and Fish chains
- 'In a Hot Country'
    - replaces 'Heart of Darkness' economy
    - inspired by central-western Africa
    - best used with sub-Tropic climate
    - a complex economy with 30 cargos and 32 industries
    - highly focussed on exporting primary cargos
    - multiple new chains and cargo types, including Cassava, Edible Oil, Nuts, Phosphate and Manganese
- 'Extreme' economy
    - renamed 'FIRS' to 'Extreme'
    - added Power Plant
    - tip: try 'Extreme' with the Busy Bee Game Script which provides cargo delivery goals


*Improved Industries*

- new industry types:
    - Copper Refinery
    - Liquids Terminal
    - Manganese Mine
    - Phosphate Mine
    - Power Plant
    - Pyrite Mine
    - Pyrite Smelter
    - Supply Yard
    - Tyre Plant
    - Vineyard
- improved industry graphics and layouts
    - Brewery - animated the flag :)
    - Builders Yard
    - Chemical Plant
    - Coal Mine
    - Coffee Estate
    - Food Processing Plant
    - Fruit Plantation
    - Iron Works
    - Rubber Plantation
    - Steel Mill
    - Vehicle Factory
- Dairies: no longer need to locate near towns
- Dredging Site:
    - now available from year 0, consistent with Quarry, which fixes broken cargo chains in some economies
    - flashing pixels removed from 1st generation graphics
- Furniture Factory: 'crates' not 't' in extra text string for
- Grain Mill:
    - renamed to Flour Mill
    - windmill version has improved graphics and layout
- Hotels: now build near any houses, rather than being restricted to 'near town sign', which could limit hotel construction in larger cities
- Lumber Yard: kiln building was broken when built on slopes
- Nitrate Mine: fixed station name
- Oil Refinery: no longer uses graphics from base set, and has additional layouts
- Quarry and Clay Pit:
    - improved graphics, including animation
    - revised industry layouts to be smaller and easier to place on the map
    - the map generator can now reliably place the quarry and clay pit at game start (previously these industry types were often missing)
    - restored the standard 1-tile gap between these industry types and any other industry
- Recycling Plant:
    - no longer randomises cargos at construction time, that was the source of too many bug reports and confusions
    - now introduced in 1978, for higher chance of seeing it in a game before getting bored
- Sawmill: additional layouts


*Improved Cargos*

- new cargo types
    - Cassava
    - Copper
    - Edible Oil
    - Maize
    - Manganese
    - Nuts
    - Phosphate
    - Pyrite Ore
    - Vehicles
- Engineering Supplies: new cargo icon
- Petrol: now named Petroleum Fuels, better reflects actual use in-game
- Recyclables: removed covered class, added bulk class
- Sugar Beet and Sugarcane:
    - removed the daft magic where Sugarcane was only in Tropic climate, and otherwise Sugarbeet was used
    - these two cargos are now completely independent from each other, don't change per climate
    - Sugar Beet appears in some economies, Sugarcane in others


*General Improvements*

- adjusted clustering behaviour for most primary industries
    - clusters are less dense, making it much easier to place stations
    - especially easier for placing supply delivery stations that should not overlap multiple industries
- adjusted industry production rates for most primary industries
    - production is generally adjusted upwards, especially for farms
    - revised production allows pickup of sensible amounts from a single industry instead of needing to aggregate several industries
    - amount of supplies required now same for farms and mines
- industry probability revised to better distribute numbers of each industry type
- processing industries that combine cargo now have a three-month delivery window instead of one month for increased output
    - this supports a wider range of transport types and play-styles, for example infrequent deliveries with ships
- added missing boost behaviour at some processing industries
- for many industries, allow location on a wider range of slopes, for better distribution on map gen
    - instead of simply disallowing all slopes, require 'effectively level' land, where only the highest corner of each tile must match the highest corner of the industry north tile
    - the benefit of this is that industries are no longer mostly crowded into flat valleys by map generator
- removed gaps in layouts from multiple industries, they look unsightly and aren't actually useful for building routes/stations
- explicitly preserve cargo slots (IDs) for passengers, mail, goods and food, default OTTD houses need them
- removed custom station rating parameter
- added parameters for adjusting 'Enhanced' and 'Gung-Ho' production behaviour at primary industries
    - amount of supplies required for each level can be set
    - increased production at each level can be set
    - affects farm-type and mine-type industries
    - port-type industries are also affected, with requirements at 10x the parameter value
- explicitly set the order of economies in parameter menu and docs (progression is from basic to more complex)
- updated online docs with images for new and changed industries
- docs now include charts showing cargo flow
- docs had some broken html
- updated translations page of docs, linking to newgrf translator
- updated readme.txt with newer vehicle sets


*Translations*

- multiple languages updated


*Codechanges*

- converted significant number of legacy C-Pre-Processor templates to python templates
- removed a large number of redundant industry templates, code is now much easier to maintain
- reduced compile time substantially (from > 2 mins to < 1 min on the test machine)
- support for single-industry compiles using make argument 'TEST_INDUSTRY=clay_pit' (swap 'clay_pit' to the required industry id)
    - single-industry compiles take around 5s on the test machine
- take advantage of increased industry limit in OpenTTD and stop trying to stuff > 64 industries into 64 slots
- grfid bumped, v2 is different enough to v1 to justify a new grfid


--------------
1.4.4 Release
--------------


*Translations*

- multiple languages updated


--------------
1.4.3 Release
--------------


*Fix*

- Machine Shop tiles were not accepting Metal (and incorrectly accepting Manufacturing Supplies instead)

*Translations*

- Croatian
- Dutch
- French
- Hungarian
- Italian


--------------
1.4.2 Release
--------------


**FIRS 1.4.2 is not savegame-compatible with any previous FIRS versions**


*New Features / Changes*

- Full FIRS economy
    - added Port, providing a direct source of Engineering Supplies
    - added Bulk Terminal, providing a direct source of Farm Supplies
- Temperate Basic economy
    - added Bulk Terminal, providing Farm Supplies, solving issue that Farm Supplies were unavailable in this economy before 1927
    - adjusted Port cargos for balance against Bulk Terminal
    - removed Fertiliser Plant, replaced by Bulk Terminal
- Arctic Basic economy
    - new cargo Paper (roughly identical to Paper cargo in default OpenTTD)
    - Paper Mill now produces Paper instead of Goods in this economy
    - removed Grain Mill industry
    - added Bulk Terminal, providing Farm Supplies, solving issue that Farm Supplies were unavailable in this economy before 1927
    - adjusted Port cargos for balance against Bulk Terminal
    - Goods is now an import cargo rather than an export cargo
    - added Iron Ore cargo and Iron Ore Mine
- Tropic Basic economy
    - new cargos Beans, Nitrates and Vehicle Parts
    - added Coffee cargo
    - removed Fish, Metal and Petrol cargos
    - removed Oil Refinery, Petrol Station and Plastics Plant
    - new Chemical Plant, Food Processing Plant, Nitrate Mine and Vehicle Factory industries
    - added Bulk Terminal, providing Farm Supplies, solving issue that Farm Supplies were unavailable in this economy before 1927
    - added Coffee Estate, replacing Fruit Plantation
    - added Arable Farm, replacing Sugar Plantation
    - adjusted Port cargos for balance against Bulk Terminal
- Introduce some industries earlier for game balance:
    - Fertiliser Plant now 1890
    - Machine Shop now 1790, to ensure Engineering Supplies and Farm Supplies more widely available from a sensible date
    - Metal Fabrication Plant now 1832
    - Petrol Pump now 1900
    - Bauxite Mine and Aluminium Plant now 1900
- improved Port graphics, now looks clearly different to Fishing Harbour
- improved Recycling Plant with smoke, improved sprites, and two new layouts
- improved Trading Post graphics
- improved Iron Works graphics and layouts
- smoke for Smithy Forge
- explain about Reycling Plant randomisation in docs, keeps catching people out


*Fixes*

- Bulk Terminal and Trading Post
    - now easier for players to build (reduced water tile checks)
    - construction states fixed
- Port construction states fixed
- Mail cargo no longer sets 'is_freight' flag to 1, caused issues with livery for mail cars and was inconsistent with default mail
- bad comparison in magic that figures out whether to use Sugar Cane or Sugar Beet


*Translation Updates*

- Afrikaans
- Catalan
- Chinese (Simplified)
- Chinese (Traditional)
- Finnish
- French
- Latin
- Norwegian (Bokmal)
- Polish
- Russian
- Scottish Gaelic
- Spanish
- Swedish


*Codechanges*

- fixed broken Makefile (planetmaker, Alberth)
- better structure for generated files in compile
- use python multiprocessing for faster python templating step
- use the PYTHON variable of the Makefile to refer to the Python interpreter (planetmaker)
- cleanup Makefile.in
- suppress Mercurial default arguments (planetmaker)
- moved docs_src to src/docs_templates, consistent with Iron Horse, Road Hog etc
- removed dead string STR_IND_SUPERMARKET
- docs handle Sugar Beet / Sugarcane climate split better, now counting them as only one cargo

1.4.0 and 1.4.1 releases weren't shipped, due to an oops with tag names not matching changelog.


--------------
1.3.0 Release
--------------


*New Features / Changes*

- New economy: Heart of Darkness
    - "Mistah Kurtz - he dead"
    - 22 cargos, including new cargos Coffee, Copper Ore, Diamonds, Rubber and Sugar
    - 21 industries, including new industries Bulk Terminal, Coffee Estate, Copper Mine, Diamond Mine, Fibre Crop Farm, Rubber Plantation, and Trading Post
    - best used with Sub-Tropic climate and many rivers
- Pre-1906 graphics for Dredging Site (DanMacK)
- Pre-1928 sprites for Arable Farm (DanMacK)
- Pre-1920 graphics for Machine Shop (DanMacK, Zephyris)
- Pre-1935 graphics for Forest (DanMacK)
- Docs improvements, including making this changelog visible in html as well as markdown text, and multiple fixes


*Fixes*

- Hotels were unexpectedly closing
- Correct order for cargo information text at Brewery
- Primary production boost required an incorrect amount of supplies


*Translations*

- Brazilian Portuguese
- Croatian
- Dutch
- Finnish
- German
- Hungarian
- Italian
- Korean
- Norwegian
- Polish
- Portugese
- Russian
- Spanish
- Swedish
- simplified Chinese
- traditional Chinese


*Codechanges*

- multiple improvements to compile environment for speed and ease of use
- refactored some industry templating to be saner

--------------
1.2.0 Release
--------------


*New Features / Changes*

- Adjusted Hotels for better game balance:
    - more expensive to build
    - lower passenger production
    - constructed by prospecting if prospecting is enabled in game settings


--------------
1.1.0 Release
--------------


*New Features / Changes*

- New graphics for Coal Mine (using sprites from DanMacK)
- Many improvements to online docs http://bundles.openttdcoop.org/firs/releases/LATEST/docs


*Translations*

- German


--------------
1.0.1 Release
--------------


*Fixes*

- Fix: serious bug with supplies behaviour for primary industries (wrong amounts for supply requirements)
- Fix: missing tile in one layout for Cement Plant


*New Features / Changes*

- Updated online docs http://bundles.openttdcoop.org/firs/releases/LATEST/docs
- Changed url for OpenTTD 'Visit Website' to point to online docs


*Translations*

- Simplified Chinese


*Codechanges*

- Refactor some CPP templating to use python instead
- Stop declaring a couple of includes in 22 different industry files, declare them once in a template instead


--------------
1.0.0 Release
--------------


*New Features / Changes*

- Feature: it's 1.0.0
- Feature: show pigs at Orchard and Piggery
- Feature: online HTML docs: http://bundles.openttdcoop.org/firs/releases/LATEST/docs


--------------
0.12.0 Release
--------------


*New Features / Changes*

- HTML docs (unfinished)
- bumped savegame min version to avoid breaking savegames


*Codechanges*

- make Ranch a separate industry to allow for customised graphics in future


*Translations Updates*

- Update: Swedish


--------------
0.11.0 Release
--------------


*New Features / Changes *

- Feature: improved construction states for Fishing Harbour and Port
- Change: updated graphics for Smithy Forge (DanMacK)
- Change: adjust base construction costs, FIRS shouldn't be trying to dictate so much what players do with their money
- Change: adjust fund costs of town industries to compensate for changed base costs


*Fixes*

- Custom station rating (set by parameter) wasn't used for some cargos


*Translations Updates*

- Update: Dutch
- Update: Hungarian
- Update: US English
- Change: Polish - improve cargo requirements string for Sugar Refinery (wojteks86)


--------------
0.10.0 Release
--------------


*New Features / Changes *

- Feature: reworked Basic Temperate economy
- Feature: add Orchard and Piggery industry in Basic Temperate
- Feature: rework Tropic Basic economy
- Feature: add General Store and remove Food Market and Hardware Store for Basic economies (graphics by DanMacK)
- Change: improve map colour for General Store
- Change: add cargo class 'covered' to Clay cargo
- Change: make Scrap Metal more visible in station list and payment rate views by changing colour (Supercheese)
- Change: improve map colour for Glass Works


*Fixes*

- Fix: bad date range check for Grain Mill during construction
- Fix: Grain Mill couldn't be built by player at all before 1870, and layout handling on construction for windmill variant was broken
- Fix: use 'crates' instead of 't' for text about Smithy Forge output cargo


*Translations Updates*

- Change: tweaks to various English strings
- Change: remove strings from multiple languages to suppress build warnings
- Fix: Typo in string command of Polish language file.
- Fix: Italian lang file had wrong lang ID
- Change: update Dutch translation
- Change: update Spanish translation
- Change: update Swedish translation
- Change: update Polish translation


--------------
0.9.x Releases
--------------


**0.9.3**

- Fix: capacity multiplier for pax should be 4 not 1
- Fix: Sugar Refinery had outdated string; also extraneous space in another string
- Fix: string for Brewery shouldn't mention Fruit in Arctic Basic economy (no fruit there)
- Change: update Croatian translation
- Change: update Dutch translation
- Change: update German translation
- Change: update Hungarian translation
- Change: update Italian translation
- Change: update Polish translation
- Change: update Spanish translation
- Change: update US English translation


**0.9.2**

- Fix: Port too cheap to fund
- Fix: Port doesn't need fund menu text
- Fix: Port wasn't checking 2nd or 3rd delivered cargo for boosts, nor processing them


**0.9.1**

- Fix: Steel Mill was producing wrong cargos


**0.9.0**

- Feature: add Port industry (Arctic Basic economy only)
- Change: some town based industries no longer set nearby station name (Pikka said it was silly)
- Change: reduce supply requirements for industries using ENSP to 21t and 84t
- Change: adjust supply requirements for industries using FMSP to 14t and 56t


*Fixes*

- Fix: wrong produced cargos at Iron Ore Mine and Coal Mine
- Fix: prevent flickering graphics at Fishing Harbour
- Fix: sprites out of place at Cement Works


*Translations Updates*

- Change: update Catalan translation
- Fix: bad control string in german lang file
- Change: plural forms in NML are now decimal like in OpenTTD lang files. Adopt the Slovakian lang file accordingly
- Change: update Hungarian translation
- Add: Slovak language file.
- Change: update US English translation


--------------
0.8.x Releases
--------------


**0.8.4**

- Fix: Portugese translation was broken when it was added (fixed by Foobar)
- Change: vehicles parked at Machine Shop no longer show flashing lights


**0.8.3**

- Fix: Sugarcane Plantation had no cargo output in non-Tropic climates
- Change: rename Sugarcane Plantation to Sugar Plantation as it produces Sugar Beet in non-Tropic climates
- Fix: remove Sugar Plantation from main FIRS economy (shouldn't be there)
- Fix: double 'per' in Biorefinery industry window text
- Portugese translation
- Updated translations for Dutch, German and Spanish


**0.8.2**

- Fix display of wrong grf name


**0.8.1**

- Fix a simple bug with cargo multipliers


**0.8.0**


*New Features*

- Reworked supplies mechanic: deliver supplies regularly for temporary production boost
- Economies, selected by parameter:
	- standard FIRS economy (31 cargos, 50 industries)
	- a basic economy to suit each climate, designed by DanMacK
		- Temperate Basic (18 cargos, 19 industries)
		- Arctic Basic (17 cargos, 19 industries)
		- Tropic Basic (18 cargos, 21 industries)
- Construction sprites for majority of industries
- Snow for windmill version of Grain Mill
- Fences for Smithy Forge
- Snow for Cement Plant, Brick Works, Recycling Depot, Recycling Plant and Machine Shop
- Snow and fences for Biorefinery and Glass Works, Metal Workshop and Textile Mill
- Snow, fences and smoke for Metal Fabrication Plant, Sugar Refinery and Stockyard
- Snow and smoke for Lumber Yard
- Smoke and animated winding wheels for Bauxite Mine
- Smoke for Lime Kiln
- Lime Kiln shows different crane / loader graphics depending on date
- Dredging Site shows steam or diesel cranes depending on date
- Aluminimum Plant, Fertiliser Plant, Junk Yard, Machine Shop have date-sensitive graphics
(most new snow sprites have been drawn by DanMacK)


*Changes*

- Adjusted various primary industry probabilities and clustering behaviours
- Remove parameters that offered primary industry production change / closing as options
- Improved names for station rating algorithm parameter options
- Removed intro date from Furniture Factory for better game balance
- Removed intro date from Paper Mill to improve gameplay balance
- Removed intro date from Stockyard to prevent broken chains
- Removed intro date from Dairy to prevent broken industry chains
- Removed intro date from Sugar Refinery to avoid breaking Sugarcane / Sugar Beet chain for early start dates
- Removed intro date from Textile Mill to avoid breaking cargo chains
- Fishing Harbours no longer required to locate near town - increases probability of being built
- Use 1825 as intro date for Dredging Site for better game balance
- Use 1830 as intro date for Oil Wells and Oil Refinery to improve game balance
- Use 1824 as intro date for Cement Plant to improve game balance
- Improved snow for Brewery, Plastics Plant and Fertiliser Plant
- Improved appearance of Food Market (DanMacK)
- [Makefile] use nml translation report script by Alberth


*Fixes*

- Recycling Depot production code was incorrect
- Palette wrong for Quarry
- Bad company colour pixels in Fishing Harbour
- Hotels were too cheap to build
- Hotel tile didn't accept passengers
- Removed STR_EXTRA_FERTILIZER_PLANT from all translations that still used {WEIGHT_SHORT}
- Missing 'chemicals' in Fertiliser Plant extra text string (alberth)
- [Makefile] Adopt NML version check to NML's new version output


*Translations Updates*

- Afrikaans
- Catalan
- Dutch
- Finnish
- French
- Hungarian
- Indonesian
- Romanian
- Spanish
- Swedish

--------------
0.7.x Releases
--------------


**0.7.5**


*Fixes*

- added missing space in fund menu 'Available from' text (OliTTD)
- remove shape checks at Quarry and Clay Pit, thereby enabling terraforming
	- increases chance that these industries appear on steep maps
- allow Hotels to build near town instead of forcing to build in town (hotels weren't built often)
- 1-tile industry spacing buffer for Sawmill didn't have cb enabled


*Changes*

- use smaller trees at food market
- improve appearance of Lumber Yard shed


*Features*

- 1-tile industry spacing for Steel Mill, Paper Mill, Oil Refinery, Iron Ore Mine, Coal Mine
	- prevents industries touching when built
- randomise initial production for industries that produce cargo
- make Forests easier to see with invisibility on - prevents machinery tile being transparent
- maximum construction dates for Iron Works (1901) and Smithy Forge (1948)
- Iron Works and Lumber Yard can now locate on slopes


*Translations Updates*

- French
- Russian
- Spanish


**0.7.4**


*Fixes*

- prevent Windmill sprites jittering when zoomed out
- Metal Fabrication Plant had wrong number of output cargos (Rhamphoryncus)
- don't need to use production cb for town industries (no more 'cargo waiting to be processed')
	- affects Builders Yard, Food Market, Hardware Store, Hotel and Petrol Pump
- only one Recycling Depot per town (otherwise population-dependent production is wrong)
- intro date for Recycling Depot was wrong
- adjust various checks for steep slopes when building industry, some fixed, some have been removed


*Changes*

- improved Cement Plant kiln animation
- Recycling Depot will always try to locate at edge of town, and avoid Recycling Plants
- introduce Biorefinery a little later


*New Features*

- introduce 'bales' as unit for Wool and Plant Fibres cargos
- educate town industries to locate more sensibly, for better gameplay and appearance
	- improves Builders Yard, Food Market, Hardware Store, Hotel and Petrol Pump
- additional layout for Metal Fabrication Plant; improved existing layouts
- add 'Available from' dates for industries that have availability restricted by date


*Translations Updates*

- Dutch
- English US
- English GB
- English AU
- French
- Hungarian


**0.7.3**

Minimum compatible version bumped to r2734 (will break compatibility with older savegames).


*Fixes*

- prevent unwanted closure of secondary industries - untested, but looks right (patch by Radmir)
- Oil Well animation was broken (patch by Terkhen / Yexo)


*Changes*

- improved appearance of Biorefinery
- improved appearance of Cement Plant


*New Features*

- station name will match industry name (except for original industries) (patch by Eddi)
- added some explanatory text to readme about small cargo amounts and primary production


*Translations Updates*

- Dutch
- Italian
- French
- Polish
- Spanish


**0.7.2**


*Fixes*

- Terraforming under some industries was possible (bug in nml), resulting in garbled graphics


*Changes*

- improved appearance of Quarry and Clay Pit


*Translations Updates*

- Dutch
- Finnish
- French
- Hungarian, Welsh, Serbian
- Polish


**0.7.1**


*Fixes*

- Recycling Depot production was wrong; production now correctly depends on town population
- Dredging Site didn't set AI routes flag, so was invisible to AIs
- Forest should not set the disaster typical for mines
- remove white pixels from Clay Pit
- AlpineClimate grf is only incompatible in the arctic climate


*Changes*

- try to make bouy for Dredging Site more visible
- set description text for station rating algorithm parameter
- improve text for 'no opening' parameter
- improved appearance of Quarry / Clay Pit graphics
- make use of CC_NON_POURABLE cargo class (Scrap Metal, Sugarcane)


*Translations Updates*

- German
- Russian
- Polish


**0.7.0**

- release


**0.7.0-beta1**

- first beta release
- intended for translators to update translations
- intended to find bugs prior to 0.7.0 release

FIRS 0.7 is *not* savegame compatible with any previous release of FIRS.

OpenTTD version 1.2.x or newer is required for FIRS 0.7.


*What's new in 0.7?*

Several hundred changes since FIRS 0.6.4


*New / Changed Industries*

- Hardware Store (accepts Building Materials, Goods)
- Metal Fabrication Plant (available 1852; accepts Metal, Chemicals, produces Building Materials)
- Recycling Depot (produces Recyclables)
- Recycling Plant (accepts Recyclables, produces two random cargos from this list: Building Materials, Chemicals, Engineering Supplies, Farm Supplies, Manufacturing Supplies, Scrap Metal)
- Hotel (accepts Food, Alcohol, Passengers, produces Passengers)

- Food Market now accepts Fruit instead of Goods
- Lime Kiln production reduced slightly for better balance of Farm Supplies chain
- Metal Foundry renamed to Metal Workshop, now also accepts Chemicals


*Removed Industries*

- None


*New / Changed Cargos*

- Introduce separate cargo labels for Sugar Beet (SGBT) and Sugarcane (SGCN).  Helps vehicle set authors provide more specific graphics.
- set Sugar Cane classes to 'bulk, non-pourable'

- Introduced Recyclables cargo, produced by Recycling Depot, accepted by Recycling Plant
- Scrap Metal now uses label SCMT instead of SCRP (due to changed classes); changed classes for Scrap Metal
- removed 'covered' class from Building Materials cargo, added 'bulk' class


*New Features*

- Parameter to prevent industry opening during game (useful for scenarios / multi-player challenges)
- Station ratings can be controlled with a parameter (default | improved | always 100%).  Affects amount of cargo distributed to stations by industries.
- Hint on possible locations for farms in the fund menu
- Petrol Pump will locate next to roads, in or out of towns
- Animation (flag) for Dairy
- Animation (pumps) for Oil Wells
- Animation (molten metal) for Iron Works
- Fences for some industries
- Graphics to show metal at Metal Foundry
- Improved appearance of Dairy
- Improved appearance of Arable Farm farmhouse
- Improved appearance of Fruit Plantation farmhouse
- Improved appearance of Furniture Factory
- Improved appearance of Dairy Farm farmhouse
- Improved appearance of Mixed Farm farmhouse
- Improved appearance of Sheep Farm farmhouse
- Improved appearance of Food Market (added trees)
- Improved appearance of Fishing Harbour (updated fishing boats, missing waves)
- Improved appearance of Grain Mill (bakery)
- Improved appearance of Grain Mill (windmill)
- Improved appearance of Glass Works
- Improved appearance of Petrol Pump
- Improved appearance of Sugar Refinery
- Improved appearance of Plastics Plant
- Improved appearance of Textile Mill
- Improved appearance of Machine Shop
- Improved appearance of Oil Wells (building added)
- Additional layout for Sheep Farm
- Additional layouts for reworked Glass Works
- Snow for Aluminium Mill
- Snow for Builders Yard
- Snow for Dairy
- Snow for Food Market
- Snow for Forge
- Snow for Grain Mill (bakery)
- Snow for Hotel
- Snow for Lime Kiln
- Snow for Petrol Pump
- Snow for Sheep Farm
- Better snow support (greeble tile) for Forest


*Fixes*

- Allow the player to also place industries where s/he wants in the scenario editor
- Builders Yard had special flag set twice
- Builders Yard construction probability was wrong
- Lime Kiln construction probability was wrong
- Store construction probability was wrong
- Flickering graphics issue solved for Fishing Harbour
- Cargo slot 1E left empty for NARS2 regearing compatibility
- Small amounts of delivered cargo could be 'lost' at secondary industries
- Always draw all ground sprites, so that in transparent mode the correct one is shown
- Industry production info text now uses litres, crates etc appropriately (previously all units were 't')
- Tile offset wrong for Forest above snowline


*Internal changes*

- FIRS converted entirely to nml instead of nfo
- Replaced all pcx graphics files with png files
- Update to grf v8


*Translations Updates*

- Hungarian translation
- Italian translation
- Polish translation
- Russian translation
- Serbian translation
- Welsh translation
- Update Croation translation
- Update Dutch translation
- Update Spanish translation
- Update German translation
- !! translations framework changed, translations require updating for 0.7.x
- Updated script to log missing strings: http://bundles.openttdcoop.org/firs/nightlies/LATEST/log/


*Documentation*

- Add GPL header to all industry files.


*Additional Compatibility checks*

- FIRS 0.7 will report requirement for OTTD 1.2.0 or r22780 or later
- Set FIRS 0.7 as minimum compatible version to prevent breaking savegames using older FIRS


--------------
0.6.x Releases
--------------


**0.6.4**

- Fix Recycling Plant availability (shouldn't have been in game)
- Partial fix for Fishing Harbours building in rivers/canals


**0.6.3**

- Updated translations for Czech, Serbian, Spanish
- Use a better 'mud' ground tile for multiple industries
- Lime Kiln uses 'mud' ground tile instead of concrete (looks better)
- Graphical improvements to Clay Pit and Quarry so they fit better with stations
- Slightly reduce Junk Yard initial production for gameplay balance
- Fix Fishing Grounds closing + production (will never change production, never close; does not use FIRS parameters)
- Fix unintended change to base costs for 'stuff with town' and 'fund town' (reset to game defaults)
- Builders Yard can build on steep slopes
- Fix disasters for Dairy Farm (removed unintended explosion disaster)
- Fix disasters for Biorefinery (use airplane disaster instead of helicopter)
- Internal improvements (suppress some non-useful build errors)
- Internal work to restore Recycling Plant (but not available in game for 0.6.3)


**0.6.2**

- Changed intro dates for Steel Mill (1873), Junk Yard (1878) and Machine Shop (1870), previously introduced in 1840s - this is for better gameplay balance against Iron Works and Smithy Forge
- Improved appearance of Aluminium Plant (additional layouts, better graphics)
- Improved appearance of Plastics Plant (uses company colours)
- Improved appearance of Brickworks (additional layouts, uses more company colours)
- Improved appearance of Lime Kiln (additional layouts, better graphics,
- Updated translations for Dutch, Serbian, Spanish
- Windmill graphics for Grain Mill (work in progress, DanMacK)
- Sawmills will try to locate close to Forests (with random chance of success) - helps link an industry chain in  games played before fast vehicles are available (Iron Works and Fishing Harbour already do this)
- Fixed missing cargo amount string for Fruit and Vegetables cargo
- Fix (untested) - Plantation and Oil Wells could incorrectly cause a subsidence
- Plastic Plant - removed easter egg ability to hide a truck station in the industry as this allowed town buildings to appear inside the industry
- Sugar Refinery no longer produces Alcohol in Tropic, this wasn't working and is too much work to support
- Updated some credits in documentation
- Multiple internal improvements and code changes with no effect on gameplay

Between releases:
- Translators can use a script that indicates what's changed in language files.
- Added a FIRS page to OpenTTD wiki http://wiki.openttd.org/FIRS


**0.6.1**

- New parameter to control maximum distance to coast for water based industries (such as Fishing Grounds, Dredging Site and Oil Platform)
- Improve display of cargo units: more consistent, better translation support, better plurals support  (issue reported by Simons Mith)
- Added cargo icons for Alcohol, Clay, Sugar Beet, Building Materials (DanMacK)
- Improved animation cycle for smoke where used
- Map colour for Iron Works improved
- Iron Works was incorrectly showing intro date in fund menu
- Improve position of Dredging Site sprites
- Dredging Site shows intro date in fund menu
- Fix numerous industries that weren't using placement checks correctly
- Updated translations for German and Serbian


**0.6**

FIRS 0.6 is *not* savegame compatible with any previous release of FIRS.


*What's new in 0.6?*

Over 150 changes since FIRS 0.5.5


*New Industries*

- Dredging Site
- Smithy Forge
- Iron Works


*Removed Industries*

- Forge


*New / Changed Cargos*

- Alcohol cargo added (cargo label: BEER) - produced by Brewery, Sugar Refinery (Tropic only) - accepted by Store
- Cargo classes changed for Wool from Piece to Piece + Covered (to match ECS spec)
- Cargo classes changed for Goods from Piece + Express to Express (to match default TTD)


*New Features*

- Fund / prospecting costs set for all industries
- Production level reduced at Fishing Grounds to better match fishing boat capacity
- Many industries try to locate a minimum distance from industries that supply / accept their cargo
- Improved appearance of Textile Mill
- New graphics for Lime Kiln
- Builders Yard / Petrol Pump - industry window no longer indicates closure in n months (they didn't close anyway)
- Smoke (animated) for many industries
- Rebalanced cargo payment rates for better gameplay
- Game will try and locate Fishing Harbours and Fishing Grounds near each other
- Graphics for Smithy Forge (Yatta / DanMacK)
- Remove large brick building from Sugar Refinery for better appearance
- Furniture Factory graphics now feature lumber and crates
- Cement plant has animation for rotating kiln (not very good, needs improving)
- Brewery uses company colour for flag
- Cargo colours improved (used in cargo payment rate graph, and in industry chain view)


*Fixes*

- Secondary industries were unexpectedly closing even when supplied with cargo (mistake with industry registers)
- Deliveries of Engineering Supplies / Farm Supplies now reported correctly in industry windows
- Mixed Farm now creates fields when built
- Boring minor error with Petrol Pump ground sprite
- Minor errors with Biorefinery tiles
- Flashing red pixel in Lumber Yard
- Boring minor error with Dairy ground sprite
- Changed callback handling to be more explicit in production code (removes one known error now, prevents future errors)
- Update attribution of graphics


*Translations*

- Some translations update
- German language now uses genders


*Documentation*

- Readme now explains what causes primary and secondary industry to close (if closure is enabled)


*Additional Compatibility checks*

- Experts Hard Industries NewGRF will be reported as incompatible
- Citybuilder NewGRFS will be reported as incompatible
- FIRS 0.6 will report requirement for OTTD 1.1.x or r21208 or later
- Set FIRS 0.6 as minimum compatible version to prevent breaking savegames using older FIRS


--------------
0.5.x Releases
--------------


**0.5.5**

- Fixed mistake where secondary industries with two output cargos would produce even with no input cargo
- Fixed mistake with production ratio registers which broke production at many industries


**0.5.4**

- Small amounts of delivered cargo no longer 'lost' at secondary industries
- Additional layouts for Biorefinery
- Additional layouts for Lumber Yard
- Fixed wrong characters in Serbian translation


**0.5.3**

- Add/update translations: Croatian, Czech, French, German, Serbian, Polish, Russian, Spanish
- Additional layout for Builders Yard
- Graphics for Sugar Refinery (replaces green box)
- Graphics for Biorefinery (replaces red box)
- Fixed Clay Pit colour in Arctic climate
- Fixed Brick Works industry window text (wrong cargos listed)
- Fixed short names for some cargos.


**0.5.2**

Fixes bug with Lime Kiln graphics.  No other changes.


**0.5.1**

Fixes bug with Forge cargo acceptance.  No other changes.


**0.5.0**

First release of FIRS 0.5.


*Important*

The grfID has changed in FIRS 0.5.  It is *not* savegame compatible with any previous release of FIRS.


*What's new in 0.5?*

Over 120 changes since FIRS 0.4


*New Industries*

- Biorefinery (no graphics yet)
- Lime Kiln (graphics unfinished)
- Builders Yard
- Brick Works


*New / Changed Cargos*

- Building Materials
- Plant Fibres (replaces Cotton and available in all climates)
- Stone (formerly Gravel)
- Removed Water cargo.  Tropic towns in Desert require Goods instead.


*Removed Industries*

- Water Plant and Water Tower
- Windmill
- Supermarket
- Retail Market
- Wholesale Market
- Gravel Pit


*New Features*

- Sand Pit is now Quarry, also produces Stone
- Significantly improved appearance of Quarry (formerly Sand Pit) and Clay Pit
- Primary industries show when maximum production of output cargos is reached (experimental)
- Cement Plant now produces Building Materials cargo instead of Goods
- Paper Mill accepts additional cargos - Clay, Chemicals
- Blacksmith renamed to Forge
- Forge accepts Wood instead of Coal
- Forge produces Engineering Supplies instead of Goods
- Bakery renamed to Grain Mill, intro date removed
- Mixed Farm now produces Plant Fibres instead of Fruit & Vegetables
- Textile Mill accepts additional cargo - Plant Fibres
- Plastics Plant accepts additional cargo - Plant Fibres
- Meat Packer renamed to Stockyard, intro date removed
- Glass Works accepts additional cargo - Chemicals
- Glass Works produces Building Materials instead of Goods
- Lumber Yard intro date removed
- Lumber Yard produces additional cargo - Building Materials
- General Store renamed to Store
- Fishing Grounds production lower to better match vehicles
- Improved minimap colours for various industries
- Bug fixed with Lumber Yard production ratios
- Various industry window texts fixed


*Translations*

- Most translations updated


-----------
0.4 Release
-----------


*Important*

The grfID has changed in FIRS 0.4.  It is *not* savegame compatible with any previous release of FIRS.


*What's new in 0.4?*

Over 220 changes since FIRS 0.3


*New Industries*

- Blacksmith (no new graphics)
- Windmill (no new graphics)
- Wholesale Market (no new graphics)
- Supermarket (no new graphics)
- Retail Market (no new graphics)
- Sugar refinery (no new graphics)


*New Cargos*

- Sugar Cane / Sugar Beet
- Petrol (formerly Fuel Oil)
- Metal (formerly Steel and Aluminium)


*Removed Industries*

- Cane Plantation (yes, we added it and removed it in the same release!)


*New Features*

- Several industries can now build on slopes
- Improved forest appearance
- Improved fruit planation appearance
- Improved sand and gravel pit appearance
- Disallow certain industries above snowline
- Disallow certain industries to build in desert
- 1 tile buffer between most industries if randomly generated
- Strict OpenTTD version requirements
- Reviewed third party set compatibility: Allow LV4 and recent TTRS
- Blacksmith now also produces farm supplies


*Translations*

- Most translations updated
- Reworked translation framework


-----------
0.3 Release
-----------


*What's new in 0.3?*

Over 80 changes since FIRS 0.2


*New Industries*

- Fishing Grounds
- Fishing Harbour


*New Cargo*

- Fish


*Removed Industries*

- Power station


*New Features*

- Set parameters for production increase/decrease and industry closure.
- Industry introduction dates in fund industry window. See how long you have to wait before you can build something.
- New industry production code


*Translations*

- Dutch
- German
- Polish


-----------
0.2 Release
-----------


*Important*

The grfID has changed in FIRS 0.2.  It is *not* savegame compatible with any previous release of FIRS.


*What's new in 0.2?*

Over 230 changes since FIRS 0.1.2


*New Industries*

- Lumber Yard: produces Engineering Supplies from Lumber and Chemicals
- Gas Station: accepts Food, Goods, Fuel Oil.  Locates in town only.  Graphics are temporary and will be replaced.

Clustering for primary industries (farms, mines, forests, plantations).  These industries will locate in clusters when constructed by the game during map generation or randomly during gameplay.  Players may build these industries anywhere during gameplay or in scenario editor.  The number of clusters is adjusted to suit the map size.  Thanks Planetmaker, Yexo and Frosch for making this feature possible.*

Anti-clustering for most secondary industries.  This prevents secondary industries of the same type locating next to each other when constructed by the game during map generation or randomly during gameplay.  Players may build these industries anywhere during gameplay or in scenario editor.*


*Clustering only available in OpenTTD nightly r19902 or newer.  Will fail gracefully in older versions.


*Tweaked numerous production levels*

- Farms now have much lower production.  Use feeder services or one large station to cover multiple farms.
- Oil wells have much higher production.  Oil was not widely available enough on the map.  More industries now use chemicals, so the oil cargo chain is a little more important in gameplay.


*Aluminium Plant production changes*

- now accepts Chemicals.  Chemicals are a small but important cargo for real-life Aluminium production, and this makes for nice gameplay.
- production is now 'combinatory'.  Delivering more than one cargo type within a month will increase output ratios (a good change requested by Terkhen to balance Aluminium Plant better against the Steel Mill).

Seriously improved map colours.  Seriously.

Space out General Stores within a town.  This uses 'prevent conflicting industry types' rather than the FIRS anti-clustering code.  Please report if the effects are weird.

Rework of strings / translation framework to correctly support UTF-8.  Entirely the work of Planetmaker and Terkhen - thanks.

Spanish translation updated (Terkhen)

Reporting of errors in-game is more useful.  Entirely the work of Planetmaker - thanks.

Fruit and Vegetables cargo had the wrong cargo classes defined.  Now fixed.

Changes to industry colours:
- more industries now use industry colours
- some industry colours are now prevented from appearing because they just suck

Completely revised graphics and layouts for:
- Fertiliser Plant
- Aluminium Plant

Snow sprites for several more industries (thanks Irwe!)

Many new / additional layouts for industries including:
- Arable Farm
- Bakery
- Brewery
- Cement Plant
- Dairy
- Furniture Factory
- Glass Works
- Junk Yard
- Machine Shop
- Plastic Plant
- Textile Mill

Improved detail and anti-aliasing of graphics for many industries including:
- Cement Plant
- Furniture Factory
- Machine Shop
- Textile Mill
...and more.
