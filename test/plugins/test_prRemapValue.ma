//Maya ASCII 2018 scene
//Name: test_prRemapValue.ma
//Last modified: Sun, Jan 27, 2019 10:42:45 PM
//Codeset: 1252
requires maya "2018";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201706261615-f9658c4cfc";
fileInfo "osv" "Microsoft Windows 8 Business Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "AE54281E-417E-5EF1-4947-E786BEDC9818";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -4.2153067725737001 4.5170653771758706 9.3746204868233143 ;
	setAttr ".r" -type "double3" -21.338352729612733 -29.000000000000224 -9.0912503328621285e-16 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "CDF2C479-4B84-00FF-CD0A-2AA2ACFF0C11";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 13.118925270765903;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "E72A95E3-4C5E-79EE-F1FD-789E0F02B8AA";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "3A3E5489-4AD3-DA36-6EDD-B3BB44C8D2B8";
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
	rename -uid "BF5DECC8-4126-ABB7-D81C-16A64E1C272C";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "2747E1DE-46F2-9A64-9C3C-92B816E131D5";
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
	rename -uid "5162C55A-4624-8911-6C71-E19FC44AB177";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "35F0DACB-4D80-9687-095F-AFA328E53572";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "locator_curve";
	rename -uid "94C8F4EC-4662-E3FD-9975-EE9BA3EB530B";
	setAttr ".t" -type "double3" 0.439094640465724 0.25737924942049872 0 ;
createNode nurbsCurve -n "locator_curveShape" -p "locator_curve";
	rename -uid "67D2D043-470E-6E74-5F7C-BC8CE42995D8";
	setAttr -k off ".v";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0 0
		-2 0 0
		-2 1 0
		-1 1 0
		-1 0 0
		;
createNode transform -n "inputMin_locator" -p "locator_curve";
	rename -uid "FA8C41AF-4D16-B742-A0BD-64AF3CF06172";
	setAttr ".t" -type "double3" -2 0 0 ;
	setAttr -l on ".tx";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "inputMin_locatorShape" -p "inputMin_locator";
	rename -uid "D6CB6A8E-4A11-7572-E6BD-CCBC7F3BBAE1";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.25 0.25 0.25 ;
createNode transform -n "inputMin_annotation" -p "inputMin_locator";
	rename -uid "B4744F7D-4CB7-715F-9EDD-13AE6533BAA0";
	setAttr -k on ".ovdt" 2;
	setAttr -k on ".ove" yes;
	setAttr ".t" -type "double3" -0.1 0.1 -0.1 ;
createNode annotationShape -n "inputMin_annotationShape" -p "inputMin_annotation";
	rename -uid "2AD76930-4FA5-94C0-FEFC-32A79E264CED";
	setAttr -k off ".v";
	setAttr ".txt" -type "string" "inputMin";
createNode transform -n "inputMax_locator" -p "locator_curve";
	rename -uid "D87B24F4-45F6-1514-7F5E-C2AFA6A0C37E";
	setAttr ".t" -type "double3" -2 1 0 ;
	setAttr -l on ".tx";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "inputMax_locatorShape" -p "inputMax_locator";
	rename -uid "BBF8EB95-497F-CAD4-6A0C-4B80AB234F7E";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.25 0.25 0.25 ;
createNode transform -n "inputMax_annotation" -p "inputMax_locator";
	rename -uid "D8EC10B1-4CFD-2F81-0D92-D4947AFD7BAA";
	setAttr -k on ".ovdt" 2;
	setAttr -k on ".ove" yes;
	setAttr ".t" -type "double3" -0.1 0.1 -0.1 ;
createNode annotationShape -n "inputMax_annotationShape" -p "inputMax_annotation";
	rename -uid "E4D456B6-4237-F7D9-2960-3B9A54A21DF3";
	setAttr -k off ".v";
	setAttr ".txt" -type "string" "inputMax";
createNode transform -n "outputMin_locator" -p "locator_curve";
	rename -uid "7790992F-47FB-086C-7441-6699B9F85958";
	setAttr ".t" -type "double3" -1 0 0 ;
	setAttr -l on ".tx";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "outputMin_locatorShape" -p "outputMin_locator";
	rename -uid "DC40CD2C-4AD3-2D77-48E9-85AC0EBAE3AA";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.25 0.25 0.25 ;
createNode transform -n "outputMin_annotation" -p "outputMin_locator";
	rename -uid "6F629142-41C5-7DF2-3C58-669F043F37CA";
	setAttr -k on ".ovdt" 2;
	setAttr -k on ".ove" yes;
	setAttr ".t" -type "double3" -0.1 0.1 -0.1 ;
createNode annotationShape -n "outputMin_annotationShape" -p "outputMin_annotation";
	rename -uid "DAD5993F-45F7-BFC7-E34F-8B85EB5FB2C1";
	setAttr -k off ".v";
	setAttr ".txt" -type "string" "outputMin";
createNode transform -n "outputMax_locator" -p "locator_curve";
	rename -uid "22639374-4B89-CCA9-C19B-C5BEFBD581A5";
	setAttr ".t" -type "double3" -1 1 0 ;
	setAttr -l on ".tx";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "outputMax_locatorShape" -p "outputMax_locator";
	rename -uid "BF76625A-459A-0300-B5DF-44B70B4E5DBC";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.25 0.25 0.25 ;
createNode transform -n "outputMax_annotation" -p "outputMax_locator";
	rename -uid "64EC4EF5-4FD3-B447-AE70-A29D6AA70ABB";
	setAttr -k on ".ovdt" 2;
	setAttr -k on ".ove" yes;
	setAttr ".t" -type "double3" -0.1 0.1 -0.1 ;
createNode annotationShape -n "outputMax_annotationShape" -p "outputMax_annotation";
	rename -uid "129C43B2-4CF3-0A89-D119-A490FF68A7E6";
	setAttr -k off ".v";
	setAttr ".txt" -type "string" "outputMax";
createNode transform -n "prRemapValue_group";
	rename -uid "295FB936-4AC0-A0AE-2F7C-5291617ED6C4";
createNode transform -n "pCube1" -p "prRemapValue_group";
	rename -uid "943588EA-4A48-9E3A-0831-D5992527E6AE";
createNode mesh -n "pCubeShape1" -p "pCube1";
	rename -uid "FAD321B9-4342-8810-A61A-339562E1C847";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".vt[0:7]"  -0.25 -0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25
		 0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25 -0.25 -0.25 -0.25 -0.25 0.25 -0.25 -0.25;
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
	setAttr ".dr" 1;
createNode transform -n "pCube2" -p "prRemapValue_group";
	rename -uid "A7776CED-4A1E-845E-71D6-3EB4F12353C7";
	setAttr ".t" -type "double3" 1 0 0 ;
createNode mesh -n "pCubeShape2" -p "pCube2";
	rename -uid "86BDAEF8-4578-08A8-9B89-298988D50A3E";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".vt[0:7]"  -0.25 -0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25
		 0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25 -0.25 -0.25 -0.25 -0.25 0.25 -0.25 -0.25;
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
	setAttr ".dr" 1;
createNode transform -n "pCube3" -p "prRemapValue_group";
	rename -uid "788134D4-4192-D072-C5F4-38AD1D8DC172";
	setAttr ".t" -type "double3" 2 0 0 ;
createNode mesh -n "pCubeShape3" -p "pCube3";
	rename -uid "7AC0258C-4F8E-5509-4851-0B908C537075";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".vt[0:7]"  -0.25 -0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25
		 0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25 -0.25 -0.25 -0.25 -0.25 0.25 -0.25 -0.25;
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
	setAttr ".dr" 1;
createNode transform -n "pCube4" -p "prRemapValue_group";
	rename -uid "39DD7E32-49B5-9D0A-3198-C6A2393A74C7";
	setAttr ".t" -type "double3" 3 0 0 ;
createNode mesh -n "pCubeShape4" -p "pCube4";
	rename -uid "81DF81F1-490C-B63A-6FB7-3DB298313DEE";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".vt[0:7]"  -0.25 -0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25
		 0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25 -0.25 -0.25 -0.25 -0.25 0.25 -0.25 -0.25;
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
	setAttr ".dr" 1;
createNode transform -n "pCube5" -p "prRemapValue_group";
	rename -uid "D85C2026-4171-58FB-5406-AD9D1C1F55B9";
	setAttr ".t" -type "double3" 4 0 0 ;
createNode mesh -n "pCubeShape5" -p "pCube5";
	rename -uid "39E2FCF4-473B-62C9-FFA3-F7AD2DA69484";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".vt[0:7]"  -0.25 -0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25
		 0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25 -0.25 -0.25 -0.25 -0.25 0.25 -0.25 -0.25;
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
	setAttr ".dr" 1;
createNode transform -n "pCube6" -p "prRemapValue_group";
	rename -uid "9B7EE5EC-480F-3514-24A0-218B14D5064F";
	setAttr ".t" -type "double3" 5 0 0 ;
createNode mesh -n "pCubeShape6" -p "pCube6";
	rename -uid "544D6C6F-4F6A-015D-A5C8-0F96CF33E3DC";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".vt[0:7]"  -0.25 -0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25
		 0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25 -0.25 -0.25 -0.25 -0.25 0.25 -0.25 -0.25;
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
	setAttr ".dr" 1;
createNode transform -n "remapValue_group";
	rename -uid "3BC4AED5-4EF1-C0E1-C7C6-AAADC99526C2";
	setAttr ".t" -type "double3" 0 0 1 ;
createNode transform -n "pCubeR1" -p "remapValue_group";
	rename -uid "5F7B0D68-4C62-8AB3-C9FB-DA8C08698533";
createNode mesh -n "pCubeRShape1" -p "pCubeR1";
	rename -uid "FB4E8D04-4DAC-56BB-95BC-989E673665C0";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".vt[0:7]"  -0.25 -0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25
		 0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25 -0.25 -0.25 -0.25 -0.25 0.25 -0.25 -0.25;
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
	setAttr ".dr" 1;
createNode transform -n "pCubeR2" -p "remapValue_group";
	rename -uid "2461BA17-4824-A047-0E93-3784D0A35EEC";
	setAttr ".t" -type "double3" 1 0.20000000298023224 0 ;
createNode mesh -n "pCubeRShape2" -p "pCubeR2";
	rename -uid "676FEB02-4CD2-624F-263A-A9B357D3730E";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".vt[0:7]"  -0.25 -0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25
		 0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25 -0.25 -0.25 -0.25 -0.25 0.25 -0.25 -0.25;
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
	setAttr ".dr" 1;
createNode transform -n "pCubeR3" -p "remapValue_group";
	rename -uid "1D294FAA-4670-8EBB-B984-4B87C055CB69";
	setAttr ".t" -type "double3" 2 0.40000000596046448 0 ;
createNode mesh -n "pCubeRShape3" -p "pCubeR3";
	rename -uid "C173E469-41B4-B493-9C57-AD81CCFE12CF";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".vt[0:7]"  -0.25 -0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25
		 0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25 -0.25 -0.25 -0.25 -0.25 0.25 -0.25 -0.25;
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
	setAttr ".dr" 1;
createNode transform -n "pCubeR4" -p "remapValue_group";
	rename -uid "C30BDC5B-4AC3-C3E0-347E-B8BADE1624AA";
	setAttr ".t" -type "double3" 3 0.60000002384185791 0 ;
createNode mesh -n "pCubeRShape4" -p "pCubeR4";
	rename -uid "94B3BE39-4EBA-7041-E370-F5BA1FEE13D2";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".vt[0:7]"  -0.25 -0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25
		 0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25 -0.25 -0.25 -0.25 -0.25 0.25 -0.25 -0.25;
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
	setAttr ".dr" 1;
createNode transform -n "pCubeR5" -p "remapValue_group";
	rename -uid "8350A4F7-4600-ADFD-7153-1588855CD1CA";
	setAttr ".t" -type "double3" 4 0.80000001192092896 0 ;
createNode mesh -n "pCubeRShape5" -p "pCubeR5";
	rename -uid "58EC2454-429C-26CA-9D75-639B0A0A7075";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".vt[0:7]"  -0.25 -0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25
		 0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25 -0.25 -0.25 -0.25 -0.25 0.25 -0.25 -0.25;
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
	setAttr ".dr" 1;
createNode transform -n "pCubeR6" -p "remapValue_group";
	rename -uid "FC3A01CA-4008-FDF7-86DD-D9861992067F";
	setAttr ".t" -type "double3" 5 1 0 ;
createNode mesh -n "pCubeRShape6" -p "pCubeR6";
	rename -uid "E9F614CF-443E-0E94-CCF0-0FA6DF6B689C";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".vt[0:7]"  -0.25 -0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25
		 0.25 0.25 0.25 -0.25 0.25 -0.25 0.25 0.25 -0.25 -0.25 -0.25 -0.25 0.25 -0.25 -0.25;
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
	setAttr ".dr" 1;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "C9E5F859-477B-E89C-74BB-D1951F71BC92";
	setAttr -s 14 ".lnk";
	setAttr -s 14 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "3927B4C5-4157-12F3-FF54-BD9A2E65B064";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "0C125931-47C9-6196-4509-1C8CE6A2EBD1";
createNode displayLayerManager -n "layerManager";
	rename -uid "40C22E67-4313-6105-BBA0-829A733B9366";
createNode displayLayer -n "defaultLayer";
	rename -uid "3AA59883-47D1-4D28-6737-90B9D3C6D774";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "EC47D789-4310-891E-4F8A-039D9110A2C0";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "AF900CE7-4056-D949-8C4C-9CB149B964ED";
	setAttr ".g" yes;
createNode blinn -n "blinn1";
	rename -uid "40DA5E3A-4D84-E930-5780-9BA5E56A240D";
createNode shadingEngine -n "blinn1SG";
	rename -uid "2B9FF89D-4F0B-3B32-878A-4DAEBD943891";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo1";
	rename -uid "12DF93A4-40E0-01BB-9268-ED9239EB7F73";
createNode blinn -n "blinn2";
	rename -uid "321076ED-4A7E-FC52-EF7C-4AB83A0FC1B6";
createNode shadingEngine -n "blinn2SG";
	rename -uid "3A466C85-4B2C-4B0C-527A-4A97006D0178";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo2";
	rename -uid "489D0905-4EE7-D10D-D7B0-4ABC6B9FE143";
createNode blinn -n "blinn3";
	rename -uid "27324A0E-4817-3F9A-EDE0-9083146AA85E";
createNode shadingEngine -n "blinn3SG";
	rename -uid "3D9950EB-488A-D303-91CF-BCB93E38FEB8";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo3";
	rename -uid "D4701B78-4BB2-A1AE-7C94-C0A75F085C70";
createNode blinn -n "blinn4";
	rename -uid "0AD5C446-49B0-9344-CE5D-F4939FB7B3AA";
createNode shadingEngine -n "blinn4SG";
	rename -uid "D880C28D-4519-E434-EEEE-AF8E299DCEB9";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo4";
	rename -uid "3693C95D-4158-E65B-9A84-09BEC4F9C2B3";
createNode blinn -n "blinn5";
	rename -uid "9BF5079C-4CC5-D522-9705-508838A2CD5D";
createNode shadingEngine -n "blinn5SG";
	rename -uid "6474E521-4659-7F0B-CC14-AE8F1432601F";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo5";
	rename -uid "A0250A75-41D6-B176-B90D-0DA583DABC9B";
createNode blinn -n "blinn6";
	rename -uid "FDB3F976-42D1-DAE3-AFE7-DFBD0049B770";
createNode shadingEngine -n "blinn6SG";
	rename -uid "68D24867-4C69-AFD5-A987-B7B4F355AB92";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo6";
	rename -uid "D2B0EDB4-44AB-5A5D-8CBA-85A7448D8F07";
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "A9AC9498-4267-D068-2AE2-EC88404C31DD";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode blinn -n "blinn7";
	rename -uid "B185158B-4917-F992-AFCD-D59999DEDCC0";
createNode shadingEngine -n "blinn7SG";
	rename -uid "0750B861-4D34-394D-BD2C-39A46C643462";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo7";
	rename -uid "136DE5DD-45CE-2F72-792A-3DAFA46409CE";
createNode blinn -n "blinn8";
	rename -uid "8B3EEF33-4151-436A-A33B-4BBFAEB57E78";
createNode shadingEngine -n "blinn8SG";
	rename -uid "648276EA-4968-AF45-8D64-2BACF50A7632";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo8";
	rename -uid "98721C9C-45CE-7193-401A-22B31234D6B5";
createNode blinn -n "blinn9";
	rename -uid "D20AD638-475D-9CDB-3EDB-5C8CA639653D";
createNode shadingEngine -n "blinn9SG";
	rename -uid "9A0B2366-483F-8DD8-7347-0F83D3E7E2EA";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo9";
	rename -uid "16B7589E-449A-28AF-CC8A-4C99F1A21F9D";
createNode blinn -n "blinn10";
	rename -uid "B24FD698-440A-090D-864C-ED9C4DC545FB";
createNode shadingEngine -n "blinn10SG";
	rename -uid "2900F9BE-49A9-37A5-860C-C89B07BDEA1A";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo10";
	rename -uid "576D05A0-4BF4-D153-307B-6A8E668D5819";
createNode blinn -n "blinn11";
	rename -uid "9D123554-4B6A-169D-6D3E-24801A8AD986";
createNode shadingEngine -n "blinn11SG";
	rename -uid "EA0F5342-4FDC-F34B-E778-C3862F26E92B";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo11";
	rename -uid "9F37DE0F-4B59-AC3A-CCD5-C58AB629D4EE";
createNode blinn -n "blinn12";
	rename -uid "78646492-46E0-92DD-C18B-5BBE8C872CAF";
createNode shadingEngine -n "blinn12SG";
	rename -uid "656A0034-4E78-EE6D-0208-398DA636301A";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo12";
	rename -uid "C99831E5-4009-2E46-4BE7-16A2BB035FDD";
createNode remapValue -n "remapValue1";
	rename -uid "E7CCD248-419C-FFDD-2696-D8A9C8DCFD6E";
	setAttr -s 2 ".vl[0:1]"  0 0 1 1 1 1;
	setAttr -s 2 ".cl";
	setAttr ".cl[0].cli" 1;
	setAttr ".cl[1].clp" 1;
	setAttr ".cl[1].clc" -type "float3" 0 1 0 ;
	setAttr ".cl[1].cli" 1;
createNode remapValue -n "remapValue2";
	rename -uid "20D79B5E-4294-94A5-31F5-009F250BAFAF";
	setAttr ".i" 0.20000000298023224;
	setAttr -s 2 ".vl[0:1]"  0 0 1 1 1 1;
	setAttr -s 2 ".cl";
	setAttr ".cl[0].cli" 1;
	setAttr ".cl[1].clp" 1;
	setAttr ".cl[1].clc" -type "float3" 0 1 0 ;
	setAttr ".cl[1].cli" 1;
createNode remapValue -n "remapValue3";
	rename -uid "0A835D94-45F9-562A-B195-27A5F0D50064";
	setAttr ".i" 0.40000000596046448;
	setAttr -s 2 ".vl[0:1]"  0 0 1 1 1 1;
	setAttr -s 2 ".cl";
	setAttr ".cl[0].cli" 1;
	setAttr ".cl[1].clp" 1;
	setAttr ".cl[1].clc" -type "float3" 0 1 0 ;
	setAttr ".cl[1].cli" 1;
createNode remapValue -n "remapValue4";
	rename -uid "0BD284B4-402A-39DC-B00B-D18AC1B5BBE5";
	setAttr ".i" 0.60000002384185791;
	setAttr -s 2 ".vl[0:1]"  0 0 1 1 1 1;
	setAttr -s 2 ".cl";
	setAttr ".cl[0].cli" 1;
	setAttr ".cl[1].clp" 1;
	setAttr ".cl[1].clc" -type "float3" 0 1 0 ;
	setAttr ".cl[1].cli" 1;
createNode remapValue -n "remapValue5";
	rename -uid "E9BE427E-43DA-998C-132F-F8BD749FD73E";
	setAttr ".i" 0.80000001192092896;
	setAttr -s 2 ".vl[0:1]"  0 0 1 1 1 1;
	setAttr -s 2 ".cl";
	setAttr ".cl[0].cli" 1;
	setAttr ".cl[1].clp" 1;
	setAttr ".cl[1].clc" -type "float3" 0 1 0 ;
	setAttr ".cl[1].cli" 1;
createNode remapValue -n "remapValue6";
	rename -uid "E2C692AC-43C6-B806-B87C-9C9FBFE63CB5";
	setAttr ".i" 1;
	setAttr -s 2 ".vl[0:1]"  0 0 1 1 1 1;
	setAttr -s 2 ".cl";
	setAttr ".cl[0].cli" 1;
	setAttr ".cl[1].clp" 1;
	setAttr ".cl[1].clc" -type "float3" 0 1 0 ;
	setAttr ".cl[1].cli" 1;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "AF35BF87-41C4-761C-5666-A59BEC0A9BE5";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -330.95236780151544 -323.80951094248991 ;
	setAttr ".tgi[0].vh" -type "double2" 317.85713022663526 338.09522466054096 ;
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
	setAttr -s 14 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 16 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :ikSystem;
	setAttr -s 4 ".sol";
connectAttr "inputMin_locatorShape.wm" "inputMin_annotationShape.dom" -na;
connectAttr "inputMax_locatorShape.wm" "inputMax_annotationShape.dom" -na;
connectAttr "outputMin_locatorShape.wm" "outputMin_annotationShape.dom" -na;
connectAttr "outputMax_locatorShape.wm" "outputMax_annotationShape.dom" -na;
connectAttr "remapValue1.ov" "pCubeR1.ty";
connectAttr "remapValue2.ov" "pCubeR2.ty";
connectAttr "remapValue3.ov" "pCubeR3.ty";
connectAttr "remapValue4.ov" "pCubeR4.ty";
connectAttr "remapValue5.ov" "pCubeR5.ty";
connectAttr "remapValue6.ov" "pCubeR6.ty";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn1SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn2SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn3SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn4SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn5SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn6SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn7SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn8SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn9SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn10SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn11SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn12SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn1SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn3SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn4SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn5SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn6SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn7SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn8SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn9SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn10SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn11SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn12SG.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "blinn1.oc" "blinn1SG.ss";
connectAttr "pCubeShape1.iog" "blinn1SG.dsm" -na;
connectAttr "blinn1SG.msg" "materialInfo1.sg";
connectAttr "blinn1.msg" "materialInfo1.m";
connectAttr "blinn2.oc" "blinn2SG.ss";
connectAttr "pCubeShape2.iog" "blinn2SG.dsm" -na;
connectAttr "blinn2SG.msg" "materialInfo2.sg";
connectAttr "blinn2.msg" "materialInfo2.m";
connectAttr "blinn3.oc" "blinn3SG.ss";
connectAttr "pCubeShape3.iog" "blinn3SG.dsm" -na;
connectAttr "blinn3SG.msg" "materialInfo3.sg";
connectAttr "blinn3.msg" "materialInfo3.m";
connectAttr "blinn4.oc" "blinn4SG.ss";
connectAttr "pCubeShape4.iog" "blinn4SG.dsm" -na;
connectAttr "blinn4SG.msg" "materialInfo4.sg";
connectAttr "blinn4.msg" "materialInfo4.m";
connectAttr "blinn5.oc" "blinn5SG.ss";
connectAttr "pCubeShape5.iog" "blinn5SG.dsm" -na;
connectAttr "blinn5SG.msg" "materialInfo5.sg";
connectAttr "blinn5.msg" "materialInfo5.m";
connectAttr "blinn6.oc" "blinn6SG.ss";
connectAttr "pCubeShape6.iog" "blinn6SG.dsm" -na;
connectAttr "blinn6SG.msg" "materialInfo6.sg";
connectAttr "blinn6.msg" "materialInfo6.m";
connectAttr "remapValue1.oc" "blinn7.c";
connectAttr "blinn7.oc" "blinn7SG.ss";
connectAttr "pCubeRShape1.iog" "blinn7SG.dsm" -na;
connectAttr "blinn7SG.msg" "materialInfo7.sg";
connectAttr "blinn7.msg" "materialInfo7.m";
connectAttr "remapValue1.msg" "materialInfo7.t" -na;
connectAttr "remapValue2.oc" "blinn8.c";
connectAttr "blinn8.oc" "blinn8SG.ss";
connectAttr "pCubeRShape2.iog" "blinn8SG.dsm" -na;
connectAttr "blinn8SG.msg" "materialInfo8.sg";
connectAttr "blinn8.msg" "materialInfo8.m";
connectAttr "remapValue2.msg" "materialInfo8.t" -na;
connectAttr "remapValue3.oc" "blinn9.c";
connectAttr "blinn9.oc" "blinn9SG.ss";
connectAttr "pCubeRShape3.iog" "blinn9SG.dsm" -na;
connectAttr "blinn9SG.msg" "materialInfo9.sg";
connectAttr "blinn9.msg" "materialInfo9.m";
connectAttr "remapValue3.msg" "materialInfo9.t" -na;
connectAttr "remapValue4.oc" "blinn10.c";
connectAttr "blinn10.oc" "blinn10SG.ss";
connectAttr "pCubeRShape4.iog" "blinn10SG.dsm" -na;
connectAttr "blinn10SG.msg" "materialInfo10.sg";
connectAttr "blinn10.msg" "materialInfo10.m";
connectAttr "remapValue4.msg" "materialInfo10.t" -na;
connectAttr "remapValue5.oc" "blinn11.c";
connectAttr "blinn11.oc" "blinn11SG.ss";
connectAttr "pCubeRShape5.iog" "blinn11SG.dsm" -na;
connectAttr "blinn11SG.msg" "materialInfo11.sg";
connectAttr "blinn11.msg" "materialInfo11.m";
connectAttr "remapValue5.msg" "materialInfo11.t" -na;
connectAttr "remapValue6.oc" "blinn12.c";
connectAttr "blinn12.oc" "blinn12SG.ss";
connectAttr "pCubeRShape6.iog" "blinn12SG.dsm" -na;
connectAttr "blinn12SG.msg" "materialInfo12.sg";
connectAttr "blinn12.msg" "materialInfo12.m";
connectAttr "remapValue6.msg" "materialInfo12.t" -na;
connectAttr "inputMin_locator.ty" "remapValue1.imn";
connectAttr "outputMax_locator.ty" "remapValue1.omx";
connectAttr "outputMin_locator.ty" "remapValue1.omn";
connectAttr "inputMax_locator.ty" "remapValue1.imx";
connectAttr "inputMin_locator.ty" "remapValue2.imn";
connectAttr "outputMax_locator.ty" "remapValue2.omx";
connectAttr "outputMin_locator.ty" "remapValue2.omn";
connectAttr "inputMax_locator.ty" "remapValue2.imx";
connectAttr "inputMin_locator.ty" "remapValue3.imn";
connectAttr "outputMax_locator.ty" "remapValue3.omx";
connectAttr "outputMin_locator.ty" "remapValue3.omn";
connectAttr "inputMax_locator.ty" "remapValue3.imx";
connectAttr "inputMin_locator.ty" "remapValue4.imn";
connectAttr "outputMax_locator.ty" "remapValue4.omx";
connectAttr "outputMin_locator.ty" "remapValue4.omn";
connectAttr "inputMax_locator.ty" "remapValue4.imx";
connectAttr "inputMin_locator.ty" "remapValue5.imn";
connectAttr "outputMax_locator.ty" "remapValue5.omx";
connectAttr "outputMin_locator.ty" "remapValue5.omn";
connectAttr "inputMax_locator.ty" "remapValue5.imx";
connectAttr "inputMin_locator.ty" "remapValue6.imn";
connectAttr "outputMax_locator.ty" "remapValue6.omx";
connectAttr "outputMin_locator.ty" "remapValue6.omn";
connectAttr "inputMax_locator.ty" "remapValue6.imx";
connectAttr "blinn1SG.pa" ":renderPartition.st" -na;
connectAttr "blinn2SG.pa" ":renderPartition.st" -na;
connectAttr "blinn3SG.pa" ":renderPartition.st" -na;
connectAttr "blinn4SG.pa" ":renderPartition.st" -na;
connectAttr "blinn5SG.pa" ":renderPartition.st" -na;
connectAttr "blinn6SG.pa" ":renderPartition.st" -na;
connectAttr "blinn7SG.pa" ":renderPartition.st" -na;
connectAttr "blinn8SG.pa" ":renderPartition.st" -na;
connectAttr "blinn9SG.pa" ":renderPartition.st" -na;
connectAttr "blinn10SG.pa" ":renderPartition.st" -na;
connectAttr "blinn11SG.pa" ":renderPartition.st" -na;
connectAttr "blinn12SG.pa" ":renderPartition.st" -na;
connectAttr "blinn1.msg" ":defaultShaderList1.s" -na;
connectAttr "blinn2.msg" ":defaultShaderList1.s" -na;
connectAttr "blinn3.msg" ":defaultShaderList1.s" -na;
connectAttr "blinn4.msg" ":defaultShaderList1.s" -na;
connectAttr "blinn5.msg" ":defaultShaderList1.s" -na;
connectAttr "blinn6.msg" ":defaultShaderList1.s" -na;
connectAttr "blinn7.msg" ":defaultShaderList1.s" -na;
connectAttr "blinn8.msg" ":defaultShaderList1.s" -na;
connectAttr "blinn9.msg" ":defaultShaderList1.s" -na;
connectAttr "blinn10.msg" ":defaultShaderList1.s" -na;
connectAttr "blinn11.msg" ":defaultShaderList1.s" -na;
connectAttr "blinn12.msg" ":defaultShaderList1.s" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of test_prRemapValue.ma
