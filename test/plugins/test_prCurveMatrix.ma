//Maya ASCII 2018ff08 scene
//Name: test_prCurveMatrix_scene.ma
//Last modified: Wed, Jan 23, 2019 11:10:00 AM
//Codeset: UTF-8
requires maya "2018ff08";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201804211841-f3d65dda2a";
fileInfo "osv" "Linux 3.10.0-693.21.1.el7.x86_64 #1 SMP Wed Mar 7 19:03:37 UTC 2018 x86_64";
fileInfo "modified-by" "prthlein";
fileInfo "modified-in" "Montreal";
createNode transform -s -n "persp";
	rename -uid "691B8541-443F-DCF3-FC3B-67B0D8980AF7";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 6.3005627751369087 4.2791406236335403 8.1226176110577661 ;
	setAttr ".r" -type "double3" -23.738352729574501 43.799999999997958 -2.2033319083286754e-15 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "5562017B-4CF0-0679-02FF-429BFEE12CDD";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 11.340932779507323;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" -2 0 0 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "2DD512B2-4247-9F3E-196F-E6BE603CDF1D";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "41E130DD-4856-7C79-AEA3-A09183F5DCBE";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "D7A8BEC4-450C-9BBA-3B9E-93A6EB2C110A";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "CCE85741-4502-C2F4-9DC7-6FBB554C9E36";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "1E1C7629-433D-FE24-2204-C1A2C21F7DE9";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "D55D6D8F-49C4-B32D-3844-2DB1A3C34C2E";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "outputPositionCurve";
	rename -uid "A1483DCF-45F9-3503-87C6-42BDF51B8202";
createNode nurbsCurve -n "outputPositionCurveShape" -p "outputPositionCurve";
	rename -uid "A4425D1F-4400-ACC3-D13A-92AF17624B17";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 3 0 no 3
		8 0 0 0 1 2 3 3 3
		6
		2.186490599060166 0 3
		0.18649059906016596 0 2
		0.18649059906016596 0.32048752317550966 0
		2.186490599060166 0 0
		2.186490599060166 -0.50200738376769616 -2
		0.18649059906016596 0 -3
		;
createNode transform -n "outputPositionCurve1";
	rename -uid "39C9DF76-44A6-79D4-A709-BF8B2356A514";
createNode nurbsCurve -n "outputPositionCurve1Shape" -p "outputPositionCurve1";
	rename -uid "6534CEB1-4343-C338-C518-1E846E33E391";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 3 0 no 3
		8 0 0 0 1 2 3 3 3
		6
		3.3766979442816325 0.03710822267608712 3
		3.5129347725740487 0.63106072232124577 2.3579273470094484
		3.2101500362370468 0.17053745823634864 0.61018753161087902
		3.4107770461186648 -0.13944796329434003 -0.81380726295080696
		3.3766979442816325 -0.67015055034585413 -2
		2.9378395741407646 0.03710822267608712 -3
		;
createNode transform -n "outputMatrixCurve";
	rename -uid "714DC1E9-455C-1B32-E1E8-B2B0108E7AF0";
createNode nurbsCurve -n "outputMatrixCurveShape" -p "outputMatrixCurve";
	rename -uid "D3754583-40A9-FFF0-5C47-2A902F105BA7";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 3 0 no 3
		8 0 0 0 1 2 3 3 3
		6
		-0.80584385418820492 -0.094050301012760684 2.9063332313917631
		-2.7475767639469102 0.67318901574339574 1.8704129630071675
		-2.6387146366285057 0.75884295067333452 0.045420437565594912
		-0.64255066321059795 0.74904978702042868 0.16884444322940526
		-0.53368853589219367 -0.061845594220643507 -1.6561480822121668
		-2.4754214456508987 -1.4356064553708447 -2.6920683505967626
		;
createNode transform -n "up_locator";
	rename -uid "F5B017D6-4A9F-34FD-CE79-449836E2D716";
	setAttr ".t" -type "double3" -0.80584385418820492 -0.094050301012760684 2.9063332313917631 ;
	setAttr ".r" -type "double3" 172.48486041209472 26.389398692287099 158.43947615455752 ;
	setAttr ".dla" yes;
	setAttr ".smd" 7;
createNode locator -n "up_locatorShape" -p "up_locator";
	rename -uid "E8BB8359-4FDB-C017-A645-8C8BFE36022A";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.5 0.5 0.5 ;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "A9AFD767-4E1D-5D21-D2BB-8D9D9267A6C0";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "00E0E0AA-4FDE-D550-40C0-AB805330681C";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "5D8F1EE3-4E9B-1104-FA2E-9FB54B5CBEAA";
createNode displayLayerManager -n "layerManager";
	rename -uid "C9C92933-4B1D-DDC0-1040-9A8214C34FF3";
createNode displayLayer -n "defaultLayer";
	rename -uid "BF3A2322-43C4-6061-94B9-D7A92A7E5362";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "9DD50080-4DEE-1C6E-2F9E-7C8CFE29EB00";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "AD69CB7C-4DE6-22F3-C2AB-A7993DF6E059";
	setAttr ".g" yes;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "0D6CFEB5-4A2F-F4BE-A8DB-1A8705CF601E";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "6994F398-4A83-FECD-9DA6-A0866034D647";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -523.8095029952043 -262.6659458628086 ;
	setAttr ".tgi[0].vh" -type "double2" 513.09521770666584 288.85642101256883 ;
	setAttr -s 3 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" -410;
	setAttr ".tgi[0].ni[0].y" 104.28571319580078;
	setAttr ".tgi[0].ni[0].nvs" 18304;
	setAttr ".tgi[0].ni[1].x" 204.28572082519531;
	setAttr ".tgi[0].ni[1].y" 104.28571319580078;
	setAttr ".tgi[0].ni[1].nvs" 18304;
	setAttr ".tgi[0].ni[2].x" 204.28572082519531;
	setAttr ".tgi[0].ni[2].y" -25.714284896850586;
	setAttr ".tgi[0].ni[2].nvs" 18304;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :defaultColorMgtGlobals;
	setAttr ".cfe" yes;
	setAttr ".cfp" -type "string" "/work/20554_SCOOBYDOO/config/ocio/config.ocio";
	setAttr ".vtn" -type "string" "Film (Monitor)";
	setAttr ".wsn" -type "string" "linear";
	setAttr ".pote" no;
	setAttr ".otn" -type "string" "Film (Monitor)";
	setAttr ".potn" -type "string" "Film (Monitor)";
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "outputMatrixCurveShape.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn"
		;
connectAttr "up_locator.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn";
connectAttr "up_locatorShape.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of test_prCurveMatrix_scene.ma
