//Maya ASCII 2018ff08 scene
//Name: prDeformPaint_003.ma
//Last modified: Thu, Jan 16, 2020 01:04:16 PM
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
	rename -uid "7C44C900-0000-9A0C-5E1F-73A70000E432";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 55.932122724305678 118.33689529118436 169.8673151861264 ;
	setAttr ".r" -type "double3" -30.305266384384893 16.20000000000066 8.2801613946400382e-16 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "7C44C900-0000-9A0C-5E1F-73A70000E433";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 234.10497643355387;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "7C44C900-0000-9A0C-5E1F-73A70000E434";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "7C44C900-0000-9A0C-5E1F-73A70000E435";
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
	rename -uid "7C44C900-0000-9A0C-5E1F-73A70000E436";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "7C44C900-0000-9A0C-5E1F-73A70000E437";
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
	rename -uid "7C44C900-0000-9A0C-5E1F-73A70000E438";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "7C44C900-0000-9A0C-5E1F-73A70000E439";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "orig";
	rename -uid "7C44C900-0000-9A0C-5E1F-73B50000E449";
	setAttr ".t" -type "double3" -30 0 0 ;
createNode mesh -n "origShape" -p "orig";
	rename -uid "7C44C900-0000-9A0C-5E1F-73B50000E44A";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.375 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".sdt" 0;
	setAttr -s 8 ".pt[0:7]" -type "float3"  -12.811541 0.5 12.811541 12.811541 
		0.5 12.811541 -12.811541 5.3762479 12.811541 12.811541 5.3762479 12.811541 -12.811541 5.3762479 -12.811541 12.811541 
		5.3762479 -12.811541 -12.811541 0.5 -12.811541 12.811541 0.5 -12.811541;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "driven_half";
	rename -uid "7C44C900-0000-9A0C-5E1F-73AE0000E443";
createNode mesh -n "driven_halfShape" -p "driven_half";
	rename -uid "7C44C900-0000-9A0C-5E1F-73AE0000E442";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.25 0.375 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".sdt" 0;
createNode mesh -n "driven_halfShapeOrig" -p "driven_half";
	rename -uid "7C44C900-0000-9A0C-5E20-A55F0001E948";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".sdt" 0;
	setAttr -s 8 ".vt[0:7]"  -13.3115406 0 13.3115406 13.3115406 0 13.3115406
		 -13.3115406 5.87624788 13.3115406 13.3115406 5.87624788 13.3115406 -13.3115406 5.8762455 -13.3115406
		 13.3115406 5.87624788 -13.3115406 -13.3115406 0 -13.3115406 13.3115406 0 -13.3115406;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "driven_one";
	rename -uid "7C44C900-0000-9A0C-5E20-A4CB0001E887";
	setAttr ".t" -type "double3" 30 0 0 ;
createNode mesh -n "driven_oneShape" -p "driven_one";
	rename -uid "7C44C900-0000-9A0C-5E20-A4CB0001E888";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.25 0.375 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode mesh -n "driven_oneShapeOrig" -p "driven_one";
	rename -uid "7C44C900-0000-9A0C-5E20-A5610001E955";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".sdt" 0;
	setAttr -s 8 ".vt[0:7]"  -13.3115406 0 13.3115406 13.3115406 0 13.3115406
		 -13.3115406 5.87624788 13.3115406 13.3115406 5.87624788 13.3115406 -13.3115406 5.87624741 -13.3115406
		 13.3115406 5.87624788 -13.3115406 -13.3115406 0 -13.3115406 13.3115406 0 -13.3115406;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "driven_two";
	rename -uid "7C44C900-0000-9A0C-5E20-A4BB0001E884";
	setAttr ".t" -type "double3" 60 0 0 ;
createNode mesh -n "driven_twoShape" -p "driven_two";
	rename -uid "7C44C900-0000-9A0C-5E20-A4BB0001E885";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode mesh -n "driven_twoShapeOrig" -p "driven_two";
	rename -uid "7C44C900-0000-9A0C-5E20-A5620001E962";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".sdt" 0;
	setAttr -s 8 ".vt[0:7]"  -13.3115406 0 13.3115406 13.3115406 0 13.3115406
		 -13.3115406 5.87624788 13.3115406 13.3115406 5.87624788 13.3115406 -13.3115406 5.87624741 -13.3115406
		 13.3115406 5.87624788 -13.3115406 -13.3115406 0 -13.3115406 13.3115406 0 -13.3115406;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "target";
	rename -uid "7C44C900-0000-9A0C-5E1F-9BFB0000E644";
	setAttr ".t" -type "double3" -30 0 -40 ;
createNode mesh -n "targetShape" -p "target";
	rename -uid "7C44C900-0000-9A0C-5E1F-9BFB0000E645";
	setAttr -k off ".v";
	setAttr -s 2 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".sdt" 0;
createNode mesh -n "targetShapeOrig" -p "target";
	rename -uid "7C44C900-0000-9A0C-5E20-A5990001E972";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".sdt" 0;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0 13.311541 0 0 13.311541 0 0 13.311541 
		0 0 13.311541 0 0 13.311541 0 0 13.311541 0 0 13.311541 0 0 13.311541 0;
	setAttr -s 8 ".vt[0:7]"  -13.3115406 -13.3115406 13.3115406 13.3115406 -13.3115406 13.3115406
		 -13.3115406 -7.4352932 13.3115406 13.3115406 -7.12568283 13.3115406 -13.3115406 11.094712257 -13.3115406
		 13.3115406 -7.12883568 -13.3115406 -13.3115406 -13.3115406 -13.3115406 13.3115406 -13.3115406 -13.3115406;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "7C44C900-0000-9A0C-5E20-A3D60001E870";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "7C44C900-0000-9A0C-5E20-A3D60001E871";
	setAttr ".bsdt[0].bscd" -type "Int32Array" 3 0 1 2 ;
	setAttr -s 3 ".bspr";
	setAttr -s 3 ".obsv";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "7C44C900-0000-9A0C-5E20-A3D60001E872";
createNode displayLayerManager -n "layerManager";
	rename -uid "7C44C900-0000-9A0C-5E20-A3D60001E873";
createNode displayLayer -n "defaultLayer";
	rename -uid "7C44C900-0000-9A0C-5E1F-73A70000E43E";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "7C44C900-0000-9A0C-5E20-A3D60001E875";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "7C44C900-0000-9A0C-5E1F-73A70000E440";
	setAttr ".g" yes;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "7C44C900-0000-9A0C-5E1F-74170000E469";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 30 -ast 1 -aet 30 ";
	setAttr ".st" 6;
createNode blendShape -n "blendShape1";
	rename -uid "7C44C900-0000-9A0C-5E20-A55F0001E947";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".w[0]"  0.5;
	setAttr ".it[0].sti" 0;
	setAttr ".it[0].siw" 1;
	setAttr ".mlid" 0;
	setAttr ".mlpr" 0;
	setAttr ".pndr[0]"  0;
	setAttr ".tgvs[0]" yes;
	setAttr ".tpvs[0]" yes;
	setAttr ".tgdt[0].cid" -type "Int32Array" 1 0 ;
	setAttr ".aal" -type "attributeAlias" {"target","weight[0]"} ;
createNode tweak -n "tweak1";
	rename -uid "7C44C900-0000-9A0C-5E20-A55F0001E949";
	setAttr ".vl[0].vt[4]" -type "float3"  9.5367432e-07 1.9073486e-06 -9.5367432e-07;
createNode objectSet -n "blendShape1Set";
	rename -uid "7C44C900-0000-9A0C-5E20-A55F0001E94A";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "blendShape1GroupId";
	rename -uid "7C44C900-0000-9A0C-5E20-A55F0001E94B";
	setAttr ".ihi" 0;
createNode groupParts -n "blendShape1GroupParts";
	rename -uid "7C44C900-0000-9A0C-5E20-A55F0001E94C";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode objectSet -n "tweakSet1";
	rename -uid "7C44C900-0000-9A0C-5E20-A55F0001E94D";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId2";
	rename -uid "7C44C900-0000-9A0C-5E20-A55F0001E94E";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts2";
	rename -uid "7C44C900-0000-9A0C-5E20-A55F0001E94F";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode blendShape -n "blendShape2";
	rename -uid "7C44C900-0000-9A0C-5E20-A5610001E954";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".w[0]"  1;
	setAttr ".it[0].sti" 0;
	setAttr ".it[0].siw" 1;
	setAttr ".mlid" 1;
	setAttr ".mlpr" 0;
	setAttr ".pndr[0]"  0;
	setAttr ".tgvs[0]" yes;
	setAttr ".tpvs[0]" yes;
	setAttr ".tgdt[0].cid" -type "Int32Array" 1 0 ;
	setAttr ".aal" -type "attributeAlias" {"target","weight[0]"} ;
createNode tweak -n "tweak2";
	rename -uid "7C44C900-0000-9A0C-5E20-A5610001E956";
	setAttr ".vl[0].vt[4]" -type "float3"  0 4.7683716e-07 4.1723251e-07;
createNode objectSet -n "blendShape2Set";
	rename -uid "7C44C900-0000-9A0C-5E20-A5610001E957";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "blendShape2GroupId";
	rename -uid "7C44C900-0000-9A0C-5E20-A5610001E958";
	setAttr ".ihi" 0;
createNode groupParts -n "blendShape2GroupParts";
	rename -uid "7C44C900-0000-9A0C-5E20-A5610001E959";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode objectSet -n "tweakSet2";
	rename -uid "7C44C900-0000-9A0C-5E20-A5610001E95A";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId4";
	rename -uid "7C44C900-0000-9A0C-5E20-A5610001E95B";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts4";
	rename -uid "7C44C900-0000-9A0C-5E20-A5610001E95C";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode blendShape -n "blendShape3";
	rename -uid "7C44C900-0000-9A0C-5E20-A5620001E961";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".w[0]"  2;
	setAttr ".it[0].sti" 0;
	setAttr ".it[0].siw" 1;
	setAttr ".mlid" 2;
	setAttr ".mlpr" 0;
	setAttr ".pndr[0]"  0;
	setAttr ".tgvs[0]" yes;
	setAttr ".tpvs[0]" yes;
	setAttr ".tgdt[0].cid" -type "Int32Array" 1 0 ;
	setAttr ".aal" -type "attributeAlias" {"target","weight[0]"} ;
createNode tweak -n "tweak3";
	rename -uid "7C44C900-0000-9A0C-5E20-A5620001E963";
createNode objectSet -n "blendShape3Set";
	rename -uid "7C44C900-0000-9A0C-5E20-A5620001E964";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "blendShape3GroupId";
	rename -uid "7C44C900-0000-9A0C-5E20-A5620001E965";
	setAttr ".ihi" 0;
createNode groupParts -n "blendShape3GroupParts";
	rename -uid "7C44C900-0000-9A0C-5E20-A5620001E966";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode objectSet -n "tweakSet3";
	rename -uid "7C44C900-0000-9A0C-5E20-A5620001E967";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId6";
	rename -uid "7C44C900-0000-9A0C-5E20-A5620001E968";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts6";
	rename -uid "7C44C900-0000-9A0C-5E20-A5620001E969";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode tweak -n "tweak4";
	rename -uid "7C44C900-0000-9A0C-5E20-A5990001E973";
createNode objectSet -n "tweakSet4";
	rename -uid "7C44C900-0000-9A0C-5E20-A5990001E974";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId7";
	rename -uid "7C44C900-0000-9A0C-5E20-A5990001E975";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts7";
	rename -uid "7C44C900-0000-9A0C-5E20-A5990001E976";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 0;
	setAttr -av -k on ".unw";
	setAttr -av -k on ".etw";
	setAttr -av -k on ".tps";
	setAttr -av -k on ".tms";
select -ne :hardwareRenderingGlobals;
	setAttr -av -k on ".ihi";
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".mhl" 16;
	setAttr -av ".ta" 3;
	setAttr -av ".aoam";
	setAttr -av ".aora";
	setAttr ".hfon" yes;
	setAttr -av ".hfs";
	setAttr -av ".hfe";
	setAttr -av ".hfa" 0;
	setAttr -av ".mbe";
	setAttr -av -k on ".mbsof";
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
	setAttr -k on ".ihi";
select -ne :initialShadingGroup;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 5 ".dsm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -av -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".w";
	setAttr -av -k on ".h";
	setAttr -av -k on ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av -k on ".dar";
	setAttr -av -k on ".ldar";
	setAttr -av -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -av -k on ".isu";
	setAttr -av -k on ".pdu";
select -ne :defaultColorMgtGlobals;
	setAttr ".cfe" yes;
	setAttr ".cfp" -type "string" "/work/20554_SCOOBYDOO/config/ocio/config.ocio";
	setAttr ".vtn" -type "string" "Film (Monitor)";
	setAttr ".wsn" -type "string" "linear";
	setAttr ".pote" no;
	setAttr ".otn" -type "string" "Film (Monitor)";
	setAttr ".potn" -type "string" "Film (Monitor)";
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k off -cb on ".ctrs" 256;
	setAttr -av -k off -cb on ".btrs" 512;
	setAttr -k off -cb on ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off -cb on ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
	setAttr -k on ".hwfr";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
select -ne :ikSystem;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".gsn";
	setAttr -k on ".gsv";
	setAttr -s 4 ".sol";
connectAttr "blendShape1GroupId.id" "driven_halfShape.iog.og[4].gid";
connectAttr "blendShape1Set.mwc" "driven_halfShape.iog.og[4].gco";
connectAttr "groupId2.id" "driven_halfShape.iog.og[5].gid";
connectAttr "tweakSet1.mwc" "driven_halfShape.iog.og[5].gco";
connectAttr "blendShape1.og[0]" "driven_halfShape.i";
connectAttr "blendShape1.it[0].vt[0]" "driven_halfShape.twl";
connectAttr "blendShape2GroupId.id" "driven_oneShape.iog.og[4].gid";
connectAttr "blendShape2Set.mwc" "driven_oneShape.iog.og[4].gco";
connectAttr "groupId4.id" "driven_oneShape.iog.og[5].gid";
connectAttr "tweakSet2.mwc" "driven_oneShape.iog.og[5].gco";
connectAttr "blendShape2.og[0]" "driven_oneShape.i";
connectAttr "blendShape2.it[0].vt[0]" "driven_oneShape.twl";
connectAttr "blendShape3GroupId.id" "driven_twoShape.iog.og[4].gid";
connectAttr "blendShape3Set.mwc" "driven_twoShape.iog.og[4].gco";
connectAttr "groupId6.id" "driven_twoShape.iog.og[5].gid";
connectAttr "tweakSet3.mwc" "driven_twoShape.iog.og[5].gco";
connectAttr "blendShape3.og[0]" "driven_twoShape.i";
connectAttr "blendShape3.it[0].vt[0]" "driven_twoShape.twl";
connectAttr "groupId7.id" "targetShape.iog.og[1].gid";
connectAttr "tweakSet4.mwc" "targetShape.iog.og[1].gco";
connectAttr "tweak4.og[0]" "targetShape.i";
connectAttr "tweak4.vl[0].vt[0]" "targetShape.twl";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "blendShape1.mlpr" "shapeEditorManager.bspr[0]";
connectAttr "blendShape2.mlpr" "shapeEditorManager.bspr[1]";
connectAttr "blendShape3.mlpr" "shapeEditorManager.bspr[2]";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "blendShape1GroupParts.og" "blendShape1.ip[0].ig";
connectAttr "blendShape1GroupId.id" "blendShape1.ip[0].gi";
connectAttr "targetShape.w" "blendShape1.it[0].itg[0].iti[6000].igt";
connectAttr "shapeEditorManager.obsv[0]" "blendShape1.tgdt[0].dpvs";
connectAttr "groupParts2.og" "tweak1.ip[0].ig";
connectAttr "groupId2.id" "tweak1.ip[0].gi";
connectAttr "blendShape1GroupId.msg" "blendShape1Set.gn" -na;
connectAttr "driven_halfShape.iog.og[4]" "blendShape1Set.dsm" -na;
connectAttr "blendShape1.msg" "blendShape1Set.ub[0]";
connectAttr "tweak1.og[0]" "blendShape1GroupParts.ig";
connectAttr "blendShape1GroupId.id" "blendShape1GroupParts.gi";
connectAttr "groupId2.msg" "tweakSet1.gn" -na;
connectAttr "driven_halfShape.iog.og[5]" "tweakSet1.dsm" -na;
connectAttr "tweak1.msg" "tweakSet1.ub[0]";
connectAttr "driven_halfShapeOrig.w" "groupParts2.ig";
connectAttr "groupId2.id" "groupParts2.gi";
connectAttr "blendShape2GroupParts.og" "blendShape2.ip[0].ig";
connectAttr "blendShape2GroupId.id" "blendShape2.ip[0].gi";
connectAttr "targetShape.w" "blendShape2.it[0].itg[0].iti[6000].igt";
connectAttr "shapeEditorManager.obsv[1]" "blendShape2.tgdt[0].dpvs";
connectAttr "groupParts4.og" "tweak2.ip[0].ig";
connectAttr "groupId4.id" "tweak2.ip[0].gi";
connectAttr "blendShape2GroupId.msg" "blendShape2Set.gn" -na;
connectAttr "driven_oneShape.iog.og[4]" "blendShape2Set.dsm" -na;
connectAttr "blendShape2.msg" "blendShape2Set.ub[0]";
connectAttr "tweak2.og[0]" "blendShape2GroupParts.ig";
connectAttr "blendShape2GroupId.id" "blendShape2GroupParts.gi";
connectAttr "groupId4.msg" "tweakSet2.gn" -na;
connectAttr "driven_oneShape.iog.og[5]" "tweakSet2.dsm" -na;
connectAttr "tweak2.msg" "tweakSet2.ub[0]";
connectAttr "driven_oneShapeOrig.w" "groupParts4.ig";
connectAttr "groupId4.id" "groupParts4.gi";
connectAttr "blendShape3GroupParts.og" "blendShape3.ip[0].ig";
connectAttr "blendShape3GroupId.id" "blendShape3.ip[0].gi";
connectAttr "targetShape.w" "blendShape3.it[0].itg[0].iti[6000].igt";
connectAttr "shapeEditorManager.obsv[2]" "blendShape3.tgdt[0].dpvs";
connectAttr "groupParts6.og" "tweak3.ip[0].ig";
connectAttr "groupId6.id" "tweak3.ip[0].gi";
connectAttr "blendShape3GroupId.msg" "blendShape3Set.gn" -na;
connectAttr "driven_twoShape.iog.og[4]" "blendShape3Set.dsm" -na;
connectAttr "blendShape3.msg" "blendShape3Set.ub[0]";
connectAttr "tweak3.og[0]" "blendShape3GroupParts.ig";
connectAttr "blendShape3GroupId.id" "blendShape3GroupParts.gi";
connectAttr "groupId6.msg" "tweakSet3.gn" -na;
connectAttr "driven_twoShape.iog.og[5]" "tweakSet3.dsm" -na;
connectAttr "tweak3.msg" "tweakSet3.ub[0]";
connectAttr "driven_twoShapeOrig.w" "groupParts6.ig";
connectAttr "groupId6.id" "groupParts6.gi";
connectAttr "groupParts7.og" "tweak4.ip[0].ig";
connectAttr "groupId7.id" "tweak4.ip[0].gi";
connectAttr "groupId7.msg" "tweakSet4.gn" -na;
connectAttr "targetShape.iog.og[1]" "tweakSet4.dsm" -na;
connectAttr "tweak4.msg" "tweakSet4.ub[0]";
connectAttr "targetShapeOrig.w" "groupParts7.ig";
connectAttr "groupId7.id" "groupParts7.gi";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "driven_halfShape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "origShape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "targetShape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "driven_twoShape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "driven_oneShape.iog" ":initialShadingGroup.dsm" -na;
// End of prDeformPaint_003.ma
